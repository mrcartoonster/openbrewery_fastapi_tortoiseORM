# -*- coding: utf-8 -*-
"""
OpenBrewery model.
"""
import ormar

from app.db import MainMeta


class Brewery(ormar.Model):
    """
    Class that represents a Brewery within the United States.

    Fhte following attributes of a brewery are stored in this table:
        id:

    """

    class Meta(MainMeta):
        """
        Init for databae, medtadata and tablename.
        """

        pass

    id: int = ormar.Integer(primary_key=True)
