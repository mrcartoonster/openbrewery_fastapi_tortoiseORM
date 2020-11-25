# -*- coding: utf-8 -*-
"""
Location of breweries endpoints.
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from tortoise.queryset import QuerySet

# from app import crud
from app.desc import brew_type
from app.models.tortoise import BrewEnum, Brewery, BrewerySchema

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
) -> List[BrewerySchema]:
    """
    Returns a list of breweries.
    """

    # TODO Refactor to make this DRY
    beer = Brewery
    booze = ""

    if any((by_city, by_type)):

        if by_city:

            if by_city.title() not in await beer.all().distinct().values_list(
                "city",
                flat=True,
            ):
                raise HTTPException(
                    status_code=400,
                    detail=f"{by_city} is not a city in this dataset.",
                )

            if isinstance(booze, QuerySet) is False:
                booze = beer.filter(
                    city=by_city.title(),
                ).limit(per_page)

            elif booze.exists():
                booze = booze.filter(city=by_city.title())

            else:
                booze = booze.filter(city=by_city.title()).limit(per_page)

        if by_type:

            if by_type not in list(BrewEnum):

                raise HTTPException(
                    status_code=422,
                    detail=f"{by_type} is not a brewery type.",
                )

            if isinstance(booze, QuerySet) is False:
                booze = beer.filter(brewery_type=by_type).limit(per_page)

            elif booze.exists():
                booze = booze.filter(brewery_type=by_type)

            else:
                booze = booze.filter(brewery_type=by_type).limit(per_page)

        return await booze
    else:
        return await beer.all().limit(per_page)
