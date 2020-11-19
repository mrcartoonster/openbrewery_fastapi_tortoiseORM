# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""
from fastapi import FastAPI

from app.api import ping
from app.db import database

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
    )

    # ormar database instance from db.py
    app.state.database = database

    # API endpoints
    app.include_router(ping.router)  # Test endpoint.

    return app


app = create_app()


@app.on_event("startup")
async def startup() -> None:
    """
    Startup ormar async database for FastAPI app.
    """
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """
    Clean shutdown of async db so eventloop is torn down cleanly.
    """
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
