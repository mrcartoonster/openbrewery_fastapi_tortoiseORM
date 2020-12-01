# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""
import sys

from environs import Env
from fastapi import FastAPI
from loguru import logger

from app.api import beer
from app.db import init_db
from app.log import log

from .desc import desc, fmt

env = Env()
env.read_env()


logger.add(
    sys.stderr,
    format=fmt,
    level="INFO",
)

logger.add(
    "logs/logged_{time:YYYY-MM-DD at hh:mm:ss A zz}.log",
    rotation="2 days",
)


def create_app() -> FastAPI:
    """
    FastAPI app factory.
    """

    # FastAPI instance
    app = FastAPI(
        title="OpenBrewery",
        description=desc,
        version="0.0.1",
        redoc_url="/",
    )

    # API endpoints
    app.include_router(beer.router, prefix="/breweries", tags=["beer"])

    # logger testings
    log.info("FastAPI created")
    logger.info("FastAPI created")
    return app


app = create_app()


@app.on_event("startup")
async def startup():
    """
    Starting up tortoise for FastAPI.
    """
    log.info("Database startup")
    init_db(app)


@app.on_event("shutdown")
async def shutdown():
    """
    Proper shutdown of Tortoise and Event loop.
    """
    log.info("Database shutdown")
    ...
