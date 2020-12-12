# -*- coding: utf-8 -*-
"""
Tortoise initializer.
 """
import ssl
from pathlib import Path

from environs import Env
from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

env = Env()
env.read_env()

cert: Path = Path("ca-certificate.crt")
ctx = ssl.create_default_context(cafile=cert.as_posix())


# Migration setup for Aerich
TORTOISE_ORM = {
    "connections": {
        "default": env("DATABASE_URL"),
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
        db_url=env("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
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
                        "database": env("DATABASE_URL"),
                        "host": (
                            "apidb-do-user-874037-0.b.db.ondigitalocean.com"
                        ),
                        "password": env("PASSWORD"),
                        "port": int(env("PORT")),
                        "user": env("USER"),
                        "ssl": ctx,
                    },
                },
            },
            "apps": {
                "models": {
                    "models": ["models.tortoise"],
                    "default_connection": "default",
                },
            },
        },
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
