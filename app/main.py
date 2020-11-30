# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""
from fastapi import FastAPI

from app.api import beer
from app.db import init_db

from .desc import desc


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

    return app


app = create_app()


@app.on_event("startup")
async def startup():
    """
    Starting up tortoise for FastAPI.
    """
    init_db(app)


@app.on_event("shutdown")
async def shutdown():
    """
    Proper shutdown of Tortoise and Event loop.
    """
    ...
