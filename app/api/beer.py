# -*- coding: utf-8 -*-
# app/api/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from typing import List

from fastapi import APIRouter

from app.api import crud
from app.models.tortoise import BrewerySchema

router = APIRouter()


@router.get("/{city}/", response_model=List[BrewerySchema])
async def by_city(city: str) -> List[BrewerySchema]:
    """
    Filter breweries by city.
    """
    city = await crud.by_city(city)

    return city
