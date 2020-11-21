# -*- coding: utf-8 -*-
"""
Database helper functions.
"""
from typing import Optional

from app.models.tortoise import Brewery


async def get_city(city: str) -> Optional[dict]:
    """
    Helper function for the app.beer.by_city endpoint.
    """
    the_city = await Brewery.filter(city=city.title())

    if the_city:
        return the_city
    else:
        return None


async def get_type(brew_type: str) -> Optional[dict]:
    """
    Helper function for the app.beer.by_type endpoint.
    """
    the_type = await Brewery.filter(brewery_type=brew_type)

    if the_type:
        return the_type
    else:
        return None
