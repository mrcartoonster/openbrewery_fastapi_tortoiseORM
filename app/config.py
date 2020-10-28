# -*- coding: utf-8 -*-
# app/config.py
"""
File that defines app's environment-specific config variables.
"""

import os

from pydantic import BaseSettings

from ..logging import logger


class Settings(BaseSettings):
    """
    Setting defaults to dev environment.
    """

    environment: str = os.getenv("ENIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings() -> BaseSettings:
    """
    Dependency injection of settings.
    """
    logger.info("Loading config settings from the environment")
    return Settings()
