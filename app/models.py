# -*- coding: utf-8 -*-
"""
OpenBrewery model.
"""
from datetime import datetime

import ormar

from app.db import MainMeta


class Brewery(ormar.Model):
    """
    Class that represents a Brewery within the United States.

    Fhte following attributes of a brewery are stored in this table:
        id: str = Unique id for brewery
        name: str = Name of brewery
        street: str = Street Address
        city: str = City brewery is located
        state: str = State brewyer is located
        postal_code: str = Zip code of brewery
        website_url: str = Brewery's website
        phone: str = Brewery's phone number
        created_at: datetime = Creation of record
        updated_at: datetime = Brewery information update
        country: str Country brewery's located in
        longitude: str = Longitude of brewery
        latitude: str = Latitude of brewery
        tags: boolean = Don't know what this is?

    """

    class Meta(MainMeta):
        """
        Init for database, medtadata and tablename.
        """

        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.Text()
    brewery_type: str = ormar.Text()
    street: str = ormar.Text(nullable=True)
    city: str = ormar.Text()
    state: str = ormar.Text()
    postal_code: str = ormar.Text()
    website_url: str = ormar.Text(nullable=True)
    phone: int = ormar.Integer(nullable=True)
    created_at: datetime = ormar.DateTime(nullable=True)
    updated_at: datetime = ormar.DateTime(nullable=True)
    country: str = ormar.Text()
    longitude: str = ormar.Text(nullable=True)
    latitude: str = ormar.Text(nullable=True)
    tags: bool = ormar.Boolean(nullable=True)
