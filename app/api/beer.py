# -*- coding: utf-8 -*-
"""
Location of breweries endpoints.
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app import crud
from app.desc import brew_type
from app.models.tortoise import BrewerySchema, BrewsEnum

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
        title="Number of breweries per page.",
        le=50,
    ),
    page: int = Query(
        0,
        title="Page number",
    ),
) -> List[BrewerySchema]:
    """
    Returns a list of breweries.
    """
    if brew_type:
        if brew_type not in list(BrewsEnum):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"{brew_type} is not a brewery type contained."
                    " Please refer to the docs to view valid brewery types."
                ),
            )

    brews = await crud.get_city(by_city, per_page, page)

    if not brews:
        raise HTTPException(
            status_code=404,
            detail=f"{by_city.title()} is not a city in the United States.",
        )

    else:
        return brews


#   @router.get(
#       "/by_type",
#       response_model=List[BrewerySchema],
#       response_model_exclude_none=True,
#   )
#   async def by_type(
#       brew_type: str = Query(
#           ...,
#           title="Brewery Type",
#       ),
#       per_page: int = Query(
#           20,
#           title="Number of breweries per page",
#           le=50,
#       ),
#       page: int = Query(
#           0,
#           title="Page number",
#       ),
#   ) -> List[BrewerySchema]:
#       """
#       Filter by type of brewery.

#       Must be one of:
#       * `micro` - Most craft breweries.
#       For example, Samual Adams is still considered a micro
#       * `nano` - An extremely small brewery
#       which typically only distributes locally.
#       * `rigional` - A regional location of an expanded brewery.
#       Ex. Sierra Nevada's Asheville, NC location.
#       * `brewpub` - A beer-focused restaurant or
#       restaurant/bar with a brewery on-premise.
#       * `large` - A very large brewery. Likely not for visitors.
#       Ex. Miller-Coors. (deprecated)
#       * `planning` - A brewery in planning or not yet opened to the public.
#       * `bar` - A bar. No brewery equipment on premise. (deprecated)
#       * `contract` - A brewery that uses another brewery's equipment.
#       * `proprietor` - Similar to contract brewing but refers more to
#       a brewery incubator.
#       * `closed` - A location which has been closed.

#       """
#       if brew_type not in list(BrewsEnum):
#           raise HTTPException(
#               status_code=400,
#               detail=(
#                   f"{brew_type} is not a brewery type contained."
#                   " Please refer to the docs to view valid brewery types."
#               ),
#           )

#       the_type = await crud.get_type(brew_type, per_page, page)

#       if not the_type:
#           raise HTTPException(
#               status_code=404,
#               detail=(
#                   f"Unfortunately, {brew_type} doesn't have any listings"
#                   " at this time."
#               ),
#           )

#       else:
#           return the_type
