# -*- coding: utf-8 -*-
"""
Brewery model.
"""
from app.db import Model


class Brewery(Model):
    """
    Brewery Table Model for Orator.
    """

    __table__ = "breweries"
    __timestamps__ = False
