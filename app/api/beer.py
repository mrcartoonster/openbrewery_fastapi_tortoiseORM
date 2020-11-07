# -*- coding: utf-8 -*-
# app/api/beer.py
"""
This will hold our FastAPI beer endpoints.
"""
from fastapi import APIRouter

from ..models.brewery import Brewery

router = APIRouter()


@router.get("/")
def breweries():
    """
    Root call the return all breweries in the API.
    """
    brews = Brewery.all()
    return brews.serialize()
