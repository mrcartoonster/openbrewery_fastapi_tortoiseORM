# -*- coding: utf-8 -*-
"""
Database helper functions.
"""
from typing import Optional

from app.models.tortoise import Brewery


async def get_city(
    city: str, per_page: int = 50, page: int = 0
) -> Optional[dict]:
    """
    Helper function for the app.beer.by_city endpoint.
    """
    the_city = (
        await Brewery.filter(city=city.title()).limit(per_page).offset(page)
    )

    if the_city:
        return the_city
    else:
        return None


async def get_type(
    brew_type: str, per_page: int = 50, page: int = 0
) -> Optional[dict]:
    """
    Helper function for the app.beer.by_type endpoint.
    """
    the_type = (
        await Brewery.filter(brewery_type=brew_type.lower())
        .limit(50)
        .offset(page)
    )

    if the_type:
        return the_type
    else:
        return None
