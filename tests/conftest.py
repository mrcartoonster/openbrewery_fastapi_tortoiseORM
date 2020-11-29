# -*- coding: utf-8 -*-
# tests/conftest.py
"""
Pytest fixtures and dummy data.
"""
import secrets

import pytest
from environs import Env
from fastapi.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_app
from app.models.tortoise import BrewEnum, Brewery

env = Env()
env.read_env()


brewenum = list(BrewEnum)

brew_ids = [secrets.choice(brewenum) for _ in brewenum]

# Breweries test names
names = [
    "Sil",
    "Che",
    "Dry",
    "Alp",
]

name_ids = [_ for _ in names]


# Brewery field names
fields = [Brewery.describe()["data_fields"][_]["name"] for _ in range(15)]
fields_id = [_ for _ in fields]

wrong_fields = ["brewery_typ", "address_", "updat"]
wrong_ids = [_ for _ in wrong_fields]


def get_settings_override():
    """
    Settings dependencies.
    """
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


@pytest.fixture(scope="session")
def client_db():
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


@pytest.fixture(params=brewenum, ids=brew_ids)
def brewenums(request):
    """
    This fixture has BrewEnum to test for validity.
    """
    return request.param


@pytest.fixture(params=names, ids=name_ids)
def naming(request):
    """
    Test brewery names list for by_name test func.
    """
    request.param


@pytest.fixture(params=fields, ids=fields_id)
def field(request):
    """
    Fields name fixtures.
    """
    return request.param


@pytest.fixture(params=wrong_fields, ids=wrong_ids)
def wrong(request):
    """
    Passing regex but wrong fields.
    """
    return request.param
