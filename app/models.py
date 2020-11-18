# -*- coding: utf-8 -*-
"""
OpenBrewery model.
"""
import ormar

from app.db import MainMeta


class Brewery(ormar.Model):
    """
    Brewery Table.
    """

    class Meta(MainMeta):
        """
        Init for databae, medtadata and tablename.
        """

        pass

    id: int = ormar.Integer(primary_key=True)
