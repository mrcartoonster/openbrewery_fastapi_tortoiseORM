# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""
from environs import Env
from fastapi import FastAPI

from app.api import beer
from app.db import init_db
from app.log import logger

from .desc import desc

# from loguru import logger


env = Env()
env.read_env()


#   logger.add(
#       sys.stderr,
#       format=fmt,
#       level="INFO",
#   )


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
    logger.info("FastAPI created")
    return app


app = create_app()


@app.on_event("startup")
async def startup():
    """
    Starting up tortoise for FastAPI.
    """
    logger.info("Database startup")
    init_db(app)


@app.on_event("shutdown")
async def shutdown():
    """
    Proper shutdown of Tortoise and Event loop.
    """
    logger.info("Database shutdown")
    ...
