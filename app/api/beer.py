# -*- coding: utf-8 -*-
"""
Location of breweries endpoints.
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

# from app import crud
from app.desc import brew_type
from app.models.tortoise import Brewery, BrewerySchema, BrewsEnum

router = APIRouter()


@router.get(
    "/",
    response_model=List[BrewerySchema],
    response_model_exclude_none=True,
)
async def breweries(
    by_city: Optional[str] = Query(
        None,
        description="Filter breweries by city.",
    ),
    by_type: Optional[str] = Query(
        None,
        description=brew_type,
    ),
    per_page: int = Query(
        20,
        description="Number of breweries per page.",
        le=50,
    ),
    page: int = Query(
        0,
        description="Page number",
    ),
) -> List[BrewerySchema]:
    """
    Returns a list of breweries.
    """

    # TODO Refactor and make this DRY
    beer = Brewery

    if by_city:

        booze = (
            beer.filter(city=by_city.title())
            .limit(per_page)
            .offset(per_page + page)
        )

    if by_type:

        if by_type not in list(BrewsEnum):

            raise HTTPException(
                status_code=400,
                detail=(
                    f"{brew_type} is not a brewery type contained."
                    " Please refer to the docs to view valid "
                    "brewery types."
                ),
            )

        booze = (
            beer.filter(brewery_type=by_type)
            .limit(
                per_page,
            )
            .offset(
                per_page + page,
            )
        )

    return await booze
