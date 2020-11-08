# -*- coding: utf-8 -*-
# app/api/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from typing import List

from fastapi import APIRouter

from ..models.brewery import Brewery
from .schemas import BrewerySchema

router = APIRouter()


@router.get(
    "/",
    response_model=List[BrewerySchema],
    response_model_exclude_none=True,
)
async def breweries() -> BrewerySchema:
    """
    Root call the return all breweries in the API.
    """
    return Brewery.all()
