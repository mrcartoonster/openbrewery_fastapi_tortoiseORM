# -*- coding: utf-8 -*-
# app/config.py
"""
File that defines app's environment-specific config variables.
"""

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn

from .logger import logger

env_path = Path("..") / ".env"

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_TEST_URL")


class Settings(BaseSettings):
    """
    Setting defaults to dev environment.
    """

    environment: str = os.getenv("ENIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: PostgresDsn = DATABASE_URL


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Dependency injection of settings.
    """
    logger.info("Loading config settings from the environment")
    return Settings()
