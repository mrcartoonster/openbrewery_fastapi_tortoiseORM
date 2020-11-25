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


def test_by_city_failing(client_db):
    """
    Testing when a city is given not located in the dataset a 400
    response is returned.
    """

    # GIVEN FastAPI GET request to breweries/ endpoint

    # WHEN GET response to invalid city to `by_city` parameter
    response = client.get("/breweries", params={"by_city": "mia"})

    # THEN assert 400 for basic error
    assert response.status_code == 400

    r_json = response.json()

    # THEN assert proper error returned
    assert r_json["detail"] == "mia is not a city in this dataset."


def test_by_type_passing(client_db):
    """
    Ensure successful request when passing correct brewery type.
    """

    # GIVEN FastAPI GET request to breweries/ endpoint

    # WHEN GET response to valid brewery type `by_type` query parameter
    response = client.get("/breweries", params={"by_type": "micro"})

    # THEN assert 200 for SUCESS
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert brewery type in response
    r_json[0]["brewery_type"] == "micro"
