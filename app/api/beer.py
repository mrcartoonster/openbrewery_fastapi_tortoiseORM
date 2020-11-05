# -*- coding: utf-8 -*-
# app/api/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from typing import List

from fastapi import APIRouter

from app.models.tortoise import Brewery, BrewerySchema

router = APIRouter()


@router.get("/", response_model=List[BrewerySchema])
async def brewery():
    """
    Getting all breweries.
    """
    return await BrewerySchema.from_queryset(Brewery.all())


@router.get("/by_city", response_model=List[BrewerySchema])
async def by_city(city: str):
    """
    Getting by city.
    """
    return await BrewerySchema.from_queryset(
        Brewery.filter(city__icontains=city.title()),
    )
