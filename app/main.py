# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""


from fastapi import FastAPI
from logger import logger

from app.api import beer
from app.db import init_db


def create_app() -> FastAPI:
    """
    FastAPI app factory.
    """
    app = FastAPI()
    app.include_router(beer.router, prefix="/beer", tags=["booze"])

    return app


app = create_app()


@app.on_event("startup")
async def start_event():
    """
    Start event handler to start tortoise.
    """
    logger.info("Starting up!")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """
    Shutting down tortoise when FastAPI is stopped.
    """
    logger.info("Shutting down!")
