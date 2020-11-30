# -*- coding: utf-8 -*-
"""
Test location for all brewery endpoints.
"""
import re

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_by_city_passing(db):
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


def test_by_city_failing(db):
    """
    Testing when a city is given not located in the dataset a 400
    response is returned.
    """

    # GIVEN FastAPI GET request to breweries/ endpoint

    # WHEN GET response to invalid city to `by_city` parameter
    response = client.get("/breweries", params={"by_city": "mia"})

    # THEN assert 400 for basic error
    assert response.status_code == 400

    response_dict = response.json()

    # THEN assert proper error returned
    assert response_dict["detail"] == "mia is not a city in this dataset."


def test_by_type_passing(db, brewenums):
    """
    Ensure successful request when passing correct brewery type.
    """

    # GIVEN FastAPI GET request to breweries/ endpoint

    # WHEN GET response to valid brewery type `by_type` query parameter
    response = client.get("/breweries", params={"by_type": brewenums})

    # THEN assert 200 for SUCESS
    assert response.status_code == 200

    response_dict = response.json()

    # THEN assert correct brewery type in response
    for _ in response_dict[:-1]:
        assert _["brewery_type"] == brewenums


def test_by_type_failing(db):
    """
    Ensure that when incorrect brewery type is requested, correct error
    response returned.
    """
    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET response to invalid brewery type `by_type` query parameter
    response = client.get("/breweries", params={"by_type": "something"})

    # THEN assert HTTPException returned
    assert response.status_code == 422

    response_dict = response.json()

    # THEN assert correct error detail is returned
    assert response_dict["detail"] == "something is not a brewery type."


def test_by_type_and_by_city_passing(db):
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


def test_by_name_passing(db):
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

    response_dict = response.json()

    # THEN assert brewery search name is returned
    for _ in response_dict[:-1]:
        assert re.search("[Ss]el", _["name"])


def test_by_state_passing(db):
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

    response_dict = response.json()

    # THEN assert brewery response only contains requested state
    assert response_dict[0]["state"] == "Florida"


def test_by_state_failing(db):
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

    response_dict = response.json()

    # THEN assert detail response is returned
    assert response_dict["detail"] == "fl is not a state in the U.S."


def test_by_postal_code_passing(db):
    """
    Ensure that when valid US zip code is given, breweries in that zip
    code are in the Response.
    """
    # GIVEN FastAPI Get request to breweries endpoint

    # WHEN GET request to `postal_code` with correct zip code
    response = client.get(
        "/breweries",
        params={"by_postal": "92121-4396"},
    )

    # THEN assert 200 is still returned
    assert response.status_code == 200

    response_dict = response.json()

    # THEN assert zip code is in respsone
    assert response_dict[0]["postal_code"] == "92121-4396"


def test_by_postal_code_regex_failing(db):
    """
    Ensure that incorrect postal code fails.
    """
    # GIVEN FASTAPI GET request to breweries endpoint

    # WHEN GET request to `postal_code` with incorrect zip code
    response = client.get(
        "/breweries",
        params={"by_postal": "912"},
    )

    # THEN asert 200 is not returned
    assert response.status_code != 200


def test_sort_passing(db, field):
    """
    Ensure when correct field is given, 200 is returned.
    """
    # GIVEN FastAPI GET request to breweries endpoint

    # WHEN GET request to `sort` with correct field
    response = client.get(
        "/breweries",
        params={"sort": field},
    )

    # THEN assert 200 is returned
    assert response.status_code == 200


def test_sort_regex_failing(db):
    """
    Ensure that regex is working when incorrect field is passed.
    """
    # GIVEN FASTAPI GET request to breweries endpoint

    # WHEN GET reqeust to `sort` with incorrect field
    response = client.get(
        "/breweries",
        params={"sort": "i"},
    )

    # THEN assert 200 is not returned
    assert response.status_code != 200


def test_sort_failing(db, wrong):
    """
    Ensure that when incorrect field is passed that passes regex, it
    fails as well at checkpoint in view function.
    """
    # GIVEN FASTAPI GET request to breweries endpoint

    # WHEN GET request to `sort` with passing regex but incorrect filed
    response = client.get(
        "/breweries",
        params={"sort": wrong},
    )

    # THEN assert 200 is not returned
    assert response.status_code != 200

    response_dict = response.json()

    # THEN assert detail error message is returned
    assert response_dict["detail"] == (
        f"'{wrong}' not a field."
        " Check BrewerySchema below for valid fields."
    )


def test_get_brewery_passing(db):
    """
    Ensure the when pased correct id, returns brewery.
    """
    # GIVEN FastAPI GEET request to breweries/{id}

    # WHEN GET request is given numeric id
    response = client.get(
        "/breweries/5494",
    )

    # THEN assert 200 is returned
    assert response.status_code == 200
