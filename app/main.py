# -*- coding: utf-8 -*-
# project/app/main.py
"""
This is where our FastAPI endpoint routers from sponsors and beers are
served.
"""


from fastapi import FastAPI

from app.api import beer


def create_app() -> FastAPI:
    """
    FastAPI app factory.
    """
    app = FastAPI()
    app.include_router(beer.router, prefix="/beer", tags=["Booze"])

    return app


app = create_app()
