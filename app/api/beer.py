# -*- coding: utf-8 -*-
# app/api/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from fastapi import APIRouter

from app.api import crud
from app.models import BeerSchema

router = APIRouter()


@router.get("/{id}", response_model=BeerSchema)
async def beer_id(id: int) -> BeerSchema:
    """
    Return Beer recipe by beer id.
    """
    recipe_id = await crud.get(id)

    return recipe_id
