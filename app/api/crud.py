# -*- coding: utf-8 -*-
# app/api/crud.py
"""
SQL helper functions for FastAPI endpoint functions.
"""
from typing import List, Optional

from app.models.tortoise import Brewery


async def breweries() -> List:
    """
    Return all breweries.
    """
    breweries = await Brewery.all().values()
    return breweries


async def by_city(city: str) -> Optional[dict]:
    """
    Helper function that queries a list of breweries by city.
    """
    the_city = city.title()  # Cities must be capitalized.

    city = await Brewery.filter(city__icontains=the_city).values()

    if city:
        return city

    return None


async def by_name(name: str) -> Optional[dict]:
    """
    Helper function that returns a list of breweries by brewery name.
    """
    pass


async def by_state(state: str) -> Optional[dict]:
    """
    Helper function that returns a list of breweries by state.
    """
    pass


async def postal_code(zip: int) -> Optional[dict]:
    """
    Helper function that returns a list of breweries by zip code.
    """
    pass


async def by_type(brew_type: str) -> Optional[dict]:
    """
    Helper function that returns a list of breweries by brewery business
    type.
    """
    pass
