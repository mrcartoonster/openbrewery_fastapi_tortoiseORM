# -*- coding: utf-8 -*-
# app/routers/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from typing import List

from fastapi import APIRouter, Query

from ..models.brewery import Brewery
from .schemas import BrewerySchema

router = APIRouter()


@router.get(
    "/",
    response_model=List[BrewerySchema],
    response_model_exclude_none=True,
)
async def breweries(
    per_page: int = Query(
        25,
        title="Breweries",
        description=(
            "Number of breweries per page. Default is 25 and max is 50"
        ),
        ge=1,
        le=50,
    ),
    page: int = Query(
        1,
        description="Select page to start on",
        ge=1,
    ),
) -> BrewerySchema:
    """
    List all breweries. By default 25 breweries per page.

    You can select to show 50 per-page. There are currently 7k+
    breweries.

    """
    breweries = Brewery.simple_paginate(per_page, page)
    return breweries.serialize()
