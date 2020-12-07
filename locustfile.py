# -*- coding: utf-8 -*-
"""
Stress tests with locusts.
"""
from locust import HttpUser, between, task


class OpenBreweryUser(HttpUser):
    """
    This user will query all breweries endpoints.
    """

    # Having this user query every 5-15 seconds
    wait_time = between(5, 15)

    @task()
    def breweries(self):
        """
        This query will just be hitting the breweries endpoint with no
        query parameters.
        """
        self.client.get("/breweries")

    @task()
    def breweries_by_city(self):
        """
        Stress test for getting breweries by city.
        """
        self.client.get("/breweries", params={"by_city": "miami"})

    @task()
    def breweries_by_name(self):
        """
        Stress test for getting breweries by name.
        """
        self.client.get("/breweries", params={"by_name": "cheaha brewing co"})

    @task()
    def breweries_by_state(self):
        """
        Stress test for getting breweries by state.
        """
        self.client.get("/breweries", params={"by_state": "florida"})

    @task()
    def breweries_by_postal(self):
        """
        Stress test by postall code.
        """
        self.client.get("/breweries", params={"by_postal": "36201-4526"})

    @task()
    def breweries_by_type(self):
        """
        Stress test by type.
        """
        self.client.get("/breweries", params={"by_type": "micro"})

    @task()
    def brewries_by_id(self):
        """
        Stress test by id.
        """
        self.client.get("/breweries/" + "12")

    @task()
    def breweries_by_search(self):
        """
        Stress test by search.
        """
        self.client.get("/breweries/search", params={"query": "dog"})
