# -*- coding: utf-8 -*-
"""
Test location for all brewery endpoints.
"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_by_city_passing(client_db):
    """
    Testing breweries endpoint by_city query parameter for successfull
    call.
    """

    # GIVEN FastAPI to breweries/ endpoint

    # WHEN requesting GET Response to valid city to `by_city` parameter
    response = client.get("/breweries", params={"by_city": "miami"})

    # THEN assert 200 for SUCCESS
    assert response.status_code == 200

    resp_json = response.json()

    # THEN assert city in response
    assert resp_json[0]["city"] == "Miami"

    # THEN assert quantity of response is equal to or less than 20
    assert len(resp_json) <= 20
