# -*- coding: utf-8 -*-
"""
Database helper functions and other helper functions.
"""
from typing import Optional

from app.models.tortoise import Brewery


async def brewery(
    by_city: Optional[str] = None,
    by_type: Optional[str] = None,
    per_page: int = 20,
    page: int = 0,
) -> Optional[dict]:
    """
    Helper function for the app.beer.breweries endpoint.
    """
    return (
        Brewery.filter(
            city=by_city,
            brewery_type=by_type,
        )
        .limit(per_page)
        .offset(page)
    )


def order(*args):
    """
    Will collect field types to order by.

    Will screen out fields that are not in Brewery automatically.

    """
    # Need to unpack the tuple!
    t = list(args)
    j = ",".join(t)
    s = j.split(",")
    return (
        _
        for _ in s
        if _ in (_["name"] for _ in Brewery.describe()["data_fields"])
        or _ in Brewery.describe()["pk_field"].values()
    )
