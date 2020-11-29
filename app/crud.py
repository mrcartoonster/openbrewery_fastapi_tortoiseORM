# -*- coding: utf-8 -*-
"""
Database helper functions and other helper functions.
"""
from enum import Enum
from typing import Optional

from app.models.tortoise import Brewery


def order(*args):
    """
    Will collect field types to order by.

    Will screen out fields that are not in Brewery automatically.

    """
    # Need to unpack the tuple!
    t = list(args)
    j = ",".join(t)
    return j.split(",")


class FieldEnum(str, Enum):
    """
    Enumarator for fields.
    """

    id = "id"
    name = "name"
    brewery_type = "brewery_type"
    street = "street"
    address_2 = "address_2"
    address_3 = "address_3"
    city = "city"
    state = "state"
    postal_code = "postal_code"
    country = "country"
    longitude = "longitude"
    latitude = "latitude"
    phone = "phone"
    website_url = "website_url"
    updated_at = "updated_at"
    created_at = "created_at"


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
