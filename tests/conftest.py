# -*- coding: utf-8 -*-
# tests/conftest.py
"""
Pytest fixtures and dummy data.
"""
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app import main
from app.config import Settings, get_settings


def get_settings_override():
    """
    Dependency injection to switch FastAPI to testing mode from
    development mode.
    """
    return Settings(testing=1)


@pytest.fixture(scope="module")
def client() -> Generator:
    """
    Setup and Teardown of Tortoise.
    """
    main.app.dependency_overrides[get_settings] = get_settings_override
    initializer(["models"])
    with TestClient(main.app) as test_client:
        yield test_client
    finalizer()
