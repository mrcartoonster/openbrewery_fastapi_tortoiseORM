# -*- coding: utf-8 -*-
# app/api/crud.py
"""
SQL helper functions for FastAPI endpoint functions.
"""
from typing import Optional

from app.models import Recipes


async def get(id: int) -> Optional[dict]:
    """
    Helper function that queries a single Beer recipe by primary key id.
    """
    recipe = await Recipes.filter(id=id).first().values

    if recipe:
        return recipe[0]

    return None
