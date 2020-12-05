# -*- coding: utf-8 -*-
"""
Database helper functions and other helper functions.
"""
from enum import Enum, unique
from typing import Optional

from app.models.tortoise import Brewery


def order(*args):
    """
    Will collect field type to order by.
    """
    # Need to unpack the tuple!
    t = list(args)
    j = ",".join(t)
    return j.split(",")


@unique
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


async def get(id: int) -> Optional[dict]:
    """
    Helper ORM function to get brewery by id.
    """
    idx = await Brewery.get_or_none(id=id)
    if idx:
        return idx

    else:
        return None


async def search(term: str) -> Optional[dict]:
    """
    Helper ORM function to get search term.
    """
    item = Brewery.filter(name__icontains=term)

    if item:
        return item

    else:
        return None
