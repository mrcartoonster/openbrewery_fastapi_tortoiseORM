# -*- coding: utf-8 -*-
"""
Brewery pydantic schema model.
"""
from enum import Enum
from typing import Optional

from pydantic import BaseModel, HttpUrl


class BrewType(str, Enum):
    """
    Accepted values in brewery brewery_type field.
    """

    closed = "closed"
    regional = "regional"
    micro = "micro"
    contract = "contract"
    brewpub = "brewpub"
    proprietor = "proprietor"
    bar = "bar"
    planning = "planning"
    large = "large"


class BrewerySchema(BaseModel):
    """
    Pydantic model for Brewery Response.
    """

    id: str
    name: str
    brewery_type: BrewType
    street: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: str
    state: Optional[str] = None
    country_province: Optional[str] = None
    postal_code: str
    website_url: Optional[HttpUrl] = None
