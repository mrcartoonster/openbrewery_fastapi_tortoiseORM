# -*- coding: utf-8 -*-
# app/db.py
"""
FastAPI Tortoise initialization for generating Tortoise schemas to
initialize in `app.main.py`.
"""
import logging

from environs import Env
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

logger = logging.getLogger(__name__)
env = Env()

env.read_env()

DEV_DB = env("DATABASE_TEST_URL")


def init_db(app: FastAPI) -> None:
    """
    Initialize database.
    """
    register_tortoise(
        app,
        db_url=DEV_DB,
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """
    Generating schemas for Tortoise model.
    """
    logger.info("Initializing Tortoise!!!")

    await Tortoise.init(
        db_url=DEV_DB,
        modules={"models": ["models.tortoise"]},
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
