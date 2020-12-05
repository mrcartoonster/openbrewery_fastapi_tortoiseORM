# -*- coding: utf-8 -*-
"""
Sponsors endpoint.
"""
import sys

from environs import Env
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.tortoise import paginate
from loguru import logger

from app.desc import fmt
from app.log import log
from app.models import Sponsor

router = APIRouter()


env = Env()
env.read_env()

logger.add(
    sys.stderr,
    format=fmt,
    level="INFO",
)


logger.add(
    "../logs/logged_{time:YYYY-MM-DD at hh:mm:ss A zz}",
    rotation="2 days",
)


@router.get(
    "/",
    response_model=Page[Sponsor],
    dependencies=[Depends(pagination_params)],
)
async def sponsor() -> Page[Sponsor]:
    """
    Returns all sponsors.
    """
    log.info("Returning Sponsors")
    logger.info("Returning Sponsors")
    return await paginate(Sponsor)
