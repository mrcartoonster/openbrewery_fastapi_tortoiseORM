# -*- coding: utf-8 -*-
# app/config.py
"""
File that defines app's environment-specific config variables.
"""
import os
from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    """
    Setting defaults to dev environment.
    """

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool
    database_url: PostgresDsn

    class Config:
        """
        Reading .env file.
        """

        env_file = Path(".env")


@lru_cache()
def get_settings() -> BaseSettings:
    """
    Dependency injection of settings.
    """
    return Settings()
