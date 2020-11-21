# -*- coding: utf-8 -*-
"""
Brewery Tortoise ORM Model.
"""
from enum import Enum

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Brews(str, Enum):
    """
    Enum class for brewery_type attribute.
    """

    micro = "micro"
    nano = "nano"
    regional = "regional"
    brewpub = "brewpub"
    large = "large"
    planning = "planning"
    bar = "bar"
    contract = "contract"
    proprietor = "proprietor"
    closed = "closed"


class Brewery(Model):
    """
    This class represents the breweries tables.

    Below are the attributes this FastAPI app will serve:
        id: int = Primary serial key
        name: str = Name of the Brewery
        brewery_type: Enum = Types of breweries:
            - micro: Most craft breweries. For example,
            Samual Adams is still considered a micro brewery.

            - nano: An extremely small brewery which typically only
            distributes locally.

            - regional: A regional location of an expanded brewery.
            Ex. Sierra Nevada's Asheville, NC location.

            - brewpub:  A beer-focused restaurant or restaurant/bar
            with a brewery on-premise.

            - large: A very large brewery. Likely not for visitors
            Ex. Miller-Coors. (deprecated)

            - planning: A brewery in planning or not yet opened to the public

            - bar: A bar. No brewry equipment on preise. (deprecated)

            - contract: A brewery that uses another brewery's equipment

            - proprietor: Similar to contract brewing but refers
            to a brewery incubator

            - closed: A location which has been closed
        street: str = Street address
        address_2: str = Extra address info
        address_3: str = Address specialty
        city: str = City where brewery is located
        state: str = State brewery's located
        postal_code: str = Breweries zip code
        created_at: datetime = Brewery's originally entered in.
        updated_at: datetime = Brewery date of last update
        country: str = Country brewery's located in
        longitude: str = longitude of brewery
        latitude: str = latitude of brewery

    """

    id = fields.IntField(pk=True)
    name = fields.TextField()
    brewery_type = fields.CharEnumField(
        enum_type=Brews,
        description="Enumator for brewery types.",
        max_length=12,
    )
    street = fields.TextField(null=True)
    address_2 = fields.TextField(null=True)
    address_3 = fields.TextField(null=True)
    city = fields.TextField()
    state = fields.TextField(null=True)
    postal_code = fields.TextField()
    website_url = fields.TextField(null=True)
    phone = fields.TextField(null=True)
    created_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(null=True)
    country = fields.TextField()
    longitude = fields.DecimalField(
        max_digits=12,
        decimal_places=8,
        null=True,
    )
    latitude = fields.DecimalField(
        max_digits=12,
        decimal_places=8,
        null=True,
    )

    class Meta:
        """
        Table information for Brewery Model.
        """

        table = "breweries"
        description = """
        Model based on OpenBreweryDB
        """


BrewerySchema = pydantic_model_creator(Brewery, name="Brewery")
