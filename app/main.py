# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""
import sys

import sentry_sdk
import timber
from environs import Env
from fastapi import FastAPI
from loguru import logger

from app.api import beer
from app.db import init_db

from .desc import desc, fmt

env = Env()
env.read_env()


sentry_sdk.init(
    env("SENTRY"),
    traces_sample_rate=1.0,
)

timber_handler = timber.TimberHandler(
    source_id=env("SOURCE"),
    api_key=env("TIMBER"),
)


logger.add(
    sys.stderr,
    format=fmt,
    level="INFO",
)

logger.add(timber_handler)


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

    # Log testings
    logger.info("FastAPI app created")
    return app


app = create_app()


@app.on_event("startup")
async def startup():
    """
    Starting up tortoise for FastAPI.
    """
    logger.info("Database Startup")
    init_db(app)


@app.on_event("shutdown")
async def shutdown():
    """
    Proper shutdown of Tortoise and Event loop.
    """
    logger.info("Shutdown")
    ...
