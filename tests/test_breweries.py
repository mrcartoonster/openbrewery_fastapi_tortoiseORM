# -*- coding: utf-8 -*-
"""
Test location for all brewery endpoints.
"""


def test_get_city(test_app_with_db):
    """
    Get 200 response when requesting a city.
    """
    # GIVEN when FastAPI breweries/by_city endpoint is requested

    # WHEN valid US City:
    response = test_app_with_db.get(
        "/breweries/by_city?city=miami&per_page=20&page=0",
    )

    # THEN status code should be 200 for success
    assert response.status_code == 200

    # THEN response should contain the city of Miami
    response_json = response.json()
    assert response_json[0]["city"] == "Miami"


def test_wrong_city(test_app_with_db):
    """
    This test will ensure that when the incorrect city's entered.

    An error is raised

    """
    # GIVEN FastAPI breweries/by_city endpoint's given

    # WHEN incorrect city is entered
    response = test_app_with_db.get(
        "/breweries/by_city?city=mia&per_page=20&page=0",
    )

    # THEN 404 Response is returned
    assert response.status_code == 404

    # THEN Recieves Error message response of:
    response_json = response.json()
    assert response_json["detail"] == (
        "Mia is not a city in the United States."
    )


def test_correct_brew_type(test_app_with_db):
    """
    Successful test for brewery/brew_type.
    """
    # GIVEN given a request to breweries/brew_type

    # WHEN correct brew type is given.
    response = test_app_with_db.get(
        "/breweries/by_type?brew_type=micro&per_page=20&page=0",
    )

    # THEN 200 Response is returned
    assert response.status_code == 200

    # THEN Response should contain brew type Micro
    response_json = response.json()
    assert response_json[0]["brewery_type"] == "micro"


def test_incorrect_brew_type(test_app_with_db):
    """
    Passing brew typer that's not in Brewery type enum.
    """
    pass
