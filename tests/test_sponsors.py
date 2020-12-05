# -*- coding: utf-8 -*-
"""
Simple tests for sponsors endpoint.
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sponsors(db):
    """
    Ensure that sponsors are returned.
    """
    # GIVEN FastAPI to /sponsors endpoint

    # WHEN Get request to endpoint
    response = client.get("/sponsors")

    # THEN assert 200 for success
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert one sponsor is located
    assert r_json["items"][0]["sponsor_name"] == "lorenanicole"


def test_sponsors_size(db):
    """
    Ensure the size returns correct number.
    """
    # GIVEN FastAPI GET request to sponsors with size correct amount is
    # returned.

    # WHEN GET request to endpoint
    response = client.get("/sponsors", params={"size": 2})

    r_json = response.json()

    # THEN assert only two sponsors are returned.
    assert len(r_json["items"]) == 2
