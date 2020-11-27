# -*- coding: utf-8 -*-
"""
Test location for all brewery endpoints.
"""
import re

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


def test_by_type_passing(client_db, brewenums):
    """
    Ensure successful request when passing correct brewery type.
    """

    # GIVEN FastAPI GET request to breweries/ endpoint

    # WHEN GET response to valid brewery type `by_type` query parameter
    response = client.get("/breweries", params={"by_type": brewenums})

    # THEN assert 200 for SUCESS
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert correct brewery type in response
    for _ in r_json[:-1]:
        assert _["brewery_type"] == brewenums


def test_by_type_failing(client_db):
    """
    Ensure that when incorrect brewery type is requested, correct error
    response returned.
    """
    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET response to invalid brewery type `by_type` query parameter
    response = client.get("/breweries", params={"by_type": "something"})

    # THEN assert HTTPException returned
    assert response.status_code == 422

    r_json = response.json()

    # THEN assert correct error detail is returned
    assert r_json["detail"] == "something is not a brewery type."


def test_by_type_and_by_city_passing(client_db):
    """
    Ensure when query parameters `by_type` and `by_city` is requeseted a
    valid city and brewery type.

    It returns a successful response

    """
    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET response to `by_city` and `by_type` query parameters
    response = client.get(
        "/breweries",
        params={"by_type": "micro", "by_city": "miami"},
    )

    # THEN assert successful response 200
    assert response.status_code == 200


def test_by_name_passing(client_db):
    """
    Ensure when correct name is passed, brewery is returned.
    """

    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET request to `by_name`
    response = client.get(
        "/breweries",
        params={"by_name": "sel"},
    )

    # THEN assert successful response 200
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert brewery search name is returned
    for _ in r_json[:-1]:
        assert re.search("[Ss]el", _["name"])


def test_by_state_passing(client_db):
    """
    Ensure correct state is passed.
    """
    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET request to `by_state`
    response = client.get(
        "/breweries",
        params={"by_state": "florida", "per_page": 2},
    )

    # THEN assert brewery search returns 200
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert brewery response only contains requested state
    assert r_json[0]["state"] == "Florida"


def test_by_state_failing(client_db):
    """
    When incorrect state is requested, 400 is returned.
    """
    # GIVEN FastaAPI Get request to breweries endpoint

    # WHEN GET request to `by_state` with incorrect state.
    response = client.get(
        "/breweries",
        params={"by_state": "fl"},
    )

    # THEN assert 400 is returned
    assert response.status_code == 400

    r_json = response.json()

    # THEN assert detail response is returned
    assert r_json["detail"] == "fl is not a state in the U.S."


def test_by_postal_code_passing(client_db):
    """
    Ensure that when valid US zip code is given, breweries in that zip
    code are in the Response.
    """
    # GIVEN FastAPI Get request to breweries endpoint

    # When GET request to `postal_code` with correct zip code
    response = client.get(
        "/breweries",
        params={"by_postal": "92121"},
    )

    # THEN assert 200 is still returned
    assert response.status_code == 200

    r_json = response.json()

    # THEN assert zip code is in respsone
    assert r_json[0]["postal_code"] == "92121"
