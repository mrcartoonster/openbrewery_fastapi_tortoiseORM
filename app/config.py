# -*- coding: utf-8 -*-
# app/config.py
"""
File that defines app's environment-specific config variables.
"""
import os
import sys
from functools import lru_cache
from pathlib import Path

from loguru import logger
from pydantic import BaseSettings, PostgresDsn

from app.desc import fmt
from app.log import log

logger.add(
    sys.stderr,
    format=fmt,
    level="INFO",
)

logger.add(
    "./logs/logged_{time:YY-MM-DD hh:mm:ss A zz}",
    rotation="2 days",
)


class Settings(BaseSettings):
    """
    Setting defaults to dev environment.
    """

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool
    database_url: PostgresDsn

    logger.info("Settings created")

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
    log.info("Loading config setting from environment.")
    logger.info("Loading config settings from environment")
    return Settings()
