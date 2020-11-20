# -*- coding: utf-8 -*-
"""
Brewery Tortoise ORM Model.
"""
from tortoise.models import Model


class Brewery(Model):
    """
    This class represents the breweries tables.

    Below are the attributes this FastAPI app will serve:
        id: int = Primary serial key
        name: str = Name of the Brewery
        brewery_type: str = Type of brewery:
            - micro: Most craft breweries. For example,
            Samual Adams is still considered a micro brewery.

            - nano: An extremely small brewery which typically only
            distributes locally.

            - regional: A regional location of an expanded brewery.
            Ex. Sierra Nevada's Asheville, NC location.

            - brewpub:  A beer-focused restaurant or restaurant/bar
            with a brewery on-premise.

    """

    pass
