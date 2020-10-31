# -*- coding: utf-8 -*-
# app/models/tortoise
"""
Tortoise database models setup.
"""
from dataclasses import dataclass
from datetime import datetime

from tortoise import fields, models


@dataclass
class Brewery(models.Model):
    """
    Model for OpenBreweryDB.

    The following attributes of a brewery are stored in this table:
        id: str = unique name of Brewery.
        name: str = Name of Brewery.
        brewery_type: str = Type of brewer:
            - micro
            - nano
            - regional
            - brewpub
            - large
            - planning
            - bar
            - contract
            - proprietor
            - closed
        street: str = Address of Brewery.
        address_2: str = Don't know what this is.
        address_3: str = Don't know what this is either.
        city: str = City brewery's located in.
        state: str = State brewery's located in.
        county_province: str = This is the province in Scotland's brewery's in.
        postal_code: str = ZipCode of brewery.
        website_url: str = Brewery's website url.
        phone: str = Brewery's phone number.
        created_at: datetime = When brewery was added to database.
        updated_at: datetime = When brewery was last updated.
        country: str = What country brewery's located in.
        longitude: float = long coordinates.
        latitude: float = lat coordinates.
        tags: bool = Don't know what this is.
        idx: int = Simple postgres serial

    """

    id: str = fields.TextField()
    name: str = fields.TextField()
    brewery_type: str = fields.TextField()
    street: str = fields.TextField(null=True)
    address_2: str = fields.TextField(null=True)
    address_3: str = fields.TextField(null=True)
    city: str = fields.TextField()
    state: str = fields.TextField(null=True)
    county_province: str = fields.TextField(null=True)
    postal_code: str = fields.TextField()
    website_url: str = fields.TextField(null=True)
    phone: str = fields.TextField()
    created_at: datetime = fields.DatetimeField(null=True)
    updated_at: datetime = fields.DatetimeField(null=True)
    country: str = fields.TextField()
    longitude: float = fields.DecimalField(
        max_digits=35,
        decimal_places=30,
        null=True,
    )
    latitude: float = fields.DecimalField(
        max_digits=35,
        decimal_places=30,
        null=True,
    )
    tags: bool = fields.BooleanField(null=True)
    idx: int = fields.IntField(pk=True)

    class Meta:
        """
        Table name and description.
        """

        table = "breweries"
        table_description = "OpenBreweryDB table for Tortoise consumption."
