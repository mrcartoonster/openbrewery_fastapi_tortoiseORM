# -*- coding: utf-8 -*-
# app/routers/schemas.py
"""
Brewery pydantic schema model.
"""
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


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
    website_url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    country: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    tags: Optional[bool] = None
    idx: int

    class Config:
        """
        Turing on ORM mode.
        """

        orm_mode = True
