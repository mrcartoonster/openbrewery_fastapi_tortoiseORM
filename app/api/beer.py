# -*- coding: utf-8 -*-
"""
Location of breweries endpoints.
"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Query
from tortoise.queryset import QuerySet

from app import crud
from app.crud import FieldEnum, order
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
    by_name: Optional[str] = Query(
        None,
        description="Filter breweries by name.",
    ),
    by_state: Optional[str] = Query(
        None,
        description="Filter breweries by state.",
    ),
    by_postal: Optional[str] = Query(
        None,
        description="Filter breweries by zip code",
        min_length=5,
        max_length=10,
        regex=r"\d{5}(-\d{4})?",
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
    sort: Optional[str] = Query(
        None,
        description="Sort the results by one field.",
        regex=r"^(-)?[inbsacplwu]\w.+|(-)?id",
    ),
) -> List[BrewerySchema]:
    """
    Returns a list of breweries.
    """

    # TODO Refactor to make this DRY
    beer = Brewery
    booze = ""

    if any((by_city, by_type, by_name, by_state, by_postal, sort)):

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
                booze = booze.filter(brewery_type=by_type).limit(per_page)

            else:
                booze = booze.filter(brewery_type=by_type).limit(per_page)

        if by_name:

            if isinstance(booze, QuerySet) is False:
                booze = beer.filter(
                    name__icontains=by_name,
                ).limit(per_page)

            elif booze.exists():
                booze = booze.filter(name__icontains=by_name).limit(per_page)

            else:
                booze = booze.filter(name__icontains=by_name).limit(per_page)

        if by_state:

            if by_state.title() not in await beer.all().distinct().values_list(
                "state",
                flat=True,
            ):
                raise HTTPException(
                    status_code=400,
                    detail=f"{by_state} is not a state in the U.S.",
                )

            if isinstance(booze, QuerySet) is False:
                booze = beer.filter(state=by_state.title()).limit(per_page)

            elif booze.exists():
                booze = booze.filter(state=by_state.title()).limit(per_page)

            else:
                booze = booze.filter(state=by_state.title()).limit(per_page)

        if by_postal:

            if isinstance(booze, QuerySet) is False:
                booze = beer.filter(postal_code__icontains=by_postal).limit(
                    per_page,
                )

            elif booze.exists():
                booze = booze.filter(postal_code__icontains=by_postal).limit(
                    per_page,
                )

            else:
                booze = booze.filter(postal_code__icontains=by_postal).limit(
                    per_page,
                )

        if sort:

            if sort.replace("-", "") not in list(FieldEnum):
                raise HTTPException(
                    status_code=400,
                    detail=(
                        f"'{sort}' not a field. Check BrewerySchema below"
                        " for valid fields."
                    ),
                )

            if isinstance(booze, QuerySet) is False:
                booze = beer.all().order_by(*order(sort)).limit(per_page)

            elif booze.exists():
                booze = booze.order_by(*order(sort)).limit(per_page)

            else:
                booze = booze.order_by(*order(sort)).limit(per_page)

        return await booze

    else:
        return await beer.all().limit(per_page)


@router.get(
    "/{id}/",
    response_model=BrewerySchema,
    response_model_exclude_none=True,
)
async def get_breweries(
    id: int = Path(
        ...,
        title="Brewery ID",
    )
) -> BrewerySchema:
    """
    Get a single brewery.
    """
    idx = await crud.get(id)

    if not idx:
        raise HTTPException(
            status_code=404,
            detail=f"{id} is not an id of a Brewery in this API.",
        )
    else:
        return idx


@router.get(
    "/search",
    response_model=List[BrewerySchema],
    response_model_exclude_none=True,
)
async def brewery_search(
    search: str = Query(
        ...,
        title="Get a list of breweries with name search.",
    )
) -> List[BrewerySchema]:
    """
    General search of brewery with search term.
    """
    item = await crud.search(search)

    if not item:
        raise HTTPException(
            status_code=404,
            detail=f"{item} didn't return anything.",
        )
    else:
        return item
