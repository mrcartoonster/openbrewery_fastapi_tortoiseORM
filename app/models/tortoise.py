# -*- coding: utf-8 -*-
"""
Tortoise database models setup.
"""
from tortoise import models


class Recipes(models.Model):
    """
    Class that represents the a collection of beer recipes.

    Table data comes from https://www.kaggle.com/jtrofe/beer-recipes
    "Brewer's Friend Beer Recipes"

    The following attributes of a beer recipe are stored in this table:
        beer_id: int = The primary key
        name: str  =  Name of the beer
        url: str = URL for beer recipe
        style: str = Type of brew
        style_id: int = Numeric id for type of brew
        size: float = Numeric ID for type of brew
        og: float = Specific gravity of wort before fermantation
        fg: float = Specific gravity of wort after fermantation
        abv: float = Alcohol by volume
        ibu: float = International Bittering Units
        color: float = Standard reference Method - light to dark
        ex. 40 = black
        boil_size: str = Fluid at beginning of boil
        boil_time: int

    """

    pass
