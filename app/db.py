# -*- coding: utf-8 -*-
"""
Tortoise initializer.
"""
import ssl

from environs import Env
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

env = Env()
env.read_env()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Migration setup for Aerich
#   TORTOISE_ORM = {
#       "connections": {
#           "default": env("DATABASE_URL"),
#       },
#       "apps": {
#           "models": {
#               "models": ["app.models.tortoise", "aerich.models"],
#               "default_connection": "default",
#           },
#       },
#   }


def init_db(app: FastAPI) -> None:
    """
    Function to register tortoise model.
    """
    register_tortoise(
        app,
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": "brewery_6pcl",
                        "host": "oregon-postgres.render.com",
                        "password": env("PASSWORD"),
                        "port": int(env("PORT")),
                        "user": env("USER"),
                        "ssl": ctx,
                    },
                },
            },
            "apps": {
                "models": {
                    "models": ["app.models.tortoise"],
                    "default_connection": "default",
                },
            },
        },
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """
    Tortoise async schema creation.
    """
    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": env("DATABASE"),
                        "host": "oregon-postgres.render.com",
                        "password": env("PASSWORD"),
                        "port": int(env("PORT")),
                        "user": env("USER"),
                        "ssl": ctx,
                    },
                },
            },
            "apps": {
                "models": {
                    "models": ["app.models.tortoise"],
                    "default_connection": "default",
                },
            },
        },
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
