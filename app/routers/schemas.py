# -*- coding: utf-8 -*-
"""
Brewery pydantic schema model.
"""
from pydantic import BaseModel


class BrewerySchema(BaseModel):
    """
    Pydantic model for Brewery Response.
    """

    name: str
