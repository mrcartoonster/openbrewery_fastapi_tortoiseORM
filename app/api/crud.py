# -*- coding: utf-8 -*-
# app/api/crud.py
"""
SQL helper functions for FastAPI endpoint functions.
"""
from typing import Optional

from app.models import Brewery


async def by_city(city: str) -> Optional[dict]:
    """
    Helper function that queries a list of breweries by city.
    """
    city = await Brewery.get(city__icontains=city).values()

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
