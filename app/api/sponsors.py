# -*- coding: utf-8 -*-
"""
Sponsors endpoint.
"""
from environs import Env
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.tortoise import paginate

from app.models.tortoise import Sponsor, SponsorSchema

router = APIRouter()


env = Env()
env.read_env()


@router.get(
    "/",
    response_model=Page[SponsorSchema],
    dependencies=[Depends(pagination_params)],
)
async def sponsor() -> Page[Sponsor]:
    """
    Returns all sponsors.
    """
    return await paginate(Sponsor)
