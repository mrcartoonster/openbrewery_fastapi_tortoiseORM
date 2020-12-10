# -*- coding: utf-8 -*-
"""
Tortoise.
"""
from environs import Env
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

env = Env()
env.read_env()


TORTOISE_ORM = {
    "connections": {
        "default": env("DB"),
    },
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    """
    Function to register tortoise model.
    """
    register_tortoise(
        app,
        db_url=env("DB"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """
    Tortoise async schema creation.
    """
    await Tortoise.init(
        db_url=env("DB"),
        modules={"models": ["models.tortoise"]},
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
