# -*- coding: utf-8 -*-
# app/db.py
"""
FastAPI Tortoise initialization for generating Tortoise schemas to
initialize in `app.main.py`.
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from logger import logger
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

env_path = Path("..") / ".env"

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATBASE_URL")


def init_db(app: FastAPI) -> None:
    """
    Initialize database.
    """
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """
    Generating schemas for Tortoise model.
    """
    logger.info("Initializing Tortoise!")

    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={"models": ["models.tortoise"]},
    )
    logger.info("Generating database schema")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
