# -*- coding: utf-8 -*-
"""
This the breweries endpoint.
"""
from typing import List

from fastapi import APIRouter

from app.models.tortoise import Brewery, BrewerySchema

router = APIRouter()


@router.get("/{city}", response_model=List[BrewerySchema])
async def by_city(city: str):
    """
    Filter breweries by city.
    """
    c = await Brewery.filter(city=city.title())
    return c


@router.get("/{type}", response_model=List[BrewerySchema])
async def by_type(type: str):
    """
    Filter by type of brewery.

    Must be one of:
    * `micro` - Most craft breweries.
    For example, Samual Adams is still considered a micro
    * `nano` - An extremely small brewery
    which typically only distributes locally.
    * `rigional` - A regional location of an expanded brewery.
    Ex. Sierra Nevada's Asheville, NC location.
    * `brewpub` - A beer-focused restaurant or
    restaurant/bar with a brewery on-premise.
    * `large` - A very large brewery. Likely not for visitors.
    Ex. Miller-Coors. (deprecated)
    * `planning` - A brewery in planning or not yet opened to the public.
    * `bar` - A bar. No brewery equipment on premise. (deprecated)
    * `contract` - A brewery that uses another brewery's equipment.
    * `proprietor` - Similar to contract brewing but refers more to
    a brewery incubator.
    * `closed` - A location which has been closed.

    """
    t = await Brewery.filter(by_type=type.title())
    return t
