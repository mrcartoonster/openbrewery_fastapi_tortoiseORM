# -*- coding: utf-8 -*-
# app/db.py
"""
FastAPI Tortoise initialization for generating Tortoise schemas to
initialize in `app.main.py`.
"""
from environs import Env
from fastapi import FastAPI
from logger import logger
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

env = Env()

env.read_env()

TORTOISE_ORM = {
    "connections": {
        "default": env("DATABASE_TEST_URL"),
    },
    "apps": {
        "models": {
            "models": ["models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    """
    Initialize database.
    """
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """
    Generating schemas for Tortoise model.
    """
    logger.info("Initializing Tortoise!")

    await Tortoise.init(
        config={
            "connections": {
                "default": env("DATABASE_TEST_URL"),
            },
            "apps": {
                "models": {
                    "models": ["app.models", "aerich.models"],
                },
            },
        },
        #   db_url=DATABASE_URL,
        #   modules={"models": ["models.tortoise", "aerich.models"]},
    )
    logger.info("Generating database schema")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
