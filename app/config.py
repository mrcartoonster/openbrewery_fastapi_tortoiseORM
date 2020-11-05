# -*- coding: utf-8 -*-
# app/config.py
"""
File that defines app's environment-specific config variables.
"""

import os
from functools import lru_cache

from environs import Env
from pydantic import BaseSettings, PostgresDsn

env = Env()
env.read_env()

DEV_DB = env("DATABASE_TEST_URL")


class Settings(BaseSettings):
    """
    Setting defaults to dev environment.
    """

    environment: str = os.getenv("ENIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: PostgresDsn = DEV_DB


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Dependency injection of settings.
    """
    return Settings()
