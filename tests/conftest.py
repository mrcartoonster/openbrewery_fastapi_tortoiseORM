# -*- coding: utf-8 -*-
# tests/conftest.py
"""
Pytest fixtures and dummy data.
"""
import pytest
from environs import Env
from fastapi.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_app

env = Env()
env.read_env()


def get_settings_override():
    return Settings(testing=1, database_url=env("DEV_DB"))


@pytest.fixture(scope="module")
def test_app():
    """
    Setup/Teardown.
    """
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:

        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    """
    Getting db to test.
    """
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=env("DEV_DB"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        yield test_client
