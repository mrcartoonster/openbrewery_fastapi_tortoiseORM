# -*- coding: utf-8 -*-
"""
Tortoise database models setup.
"""
from tortoise import fields, models


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
        boil_time: int = Time wort is boild
        boil_gravity: str = Specific gravity of wort before the boil
        efficiency: int = Beer mash extraction efficiency - extracting sugars
        from the grain during mash
        mash_thickness: str = Amount of water per pound of grain
        sugar_scale: str = Scale to determine the concentration of
        dissolved solids in wort
        brew_method: str = various techniques for brewing
        pitch_rate: str = Yeast added to the fermentor
        per gravity unit - M cells/m/deg P
        primary_temp: str = Temperature at the fermenting stage
        priming_sugar: str = Priming sugar type used if sugar is used
        priming_amount: str =  Amount of priming sugar used if sugar was used
        user_id: int = ForeignKey to another table. Will be removed.

    """

    beer_id = fields.SmallIntField(pk=True)
    name = fields.TextField(null=True)
    url = fields.TextField()
    style = fields.TextField(null=True)
    style_id = fields.SmallIntField()
    size = fields.FloatField()
    og = fields.FloatField()
