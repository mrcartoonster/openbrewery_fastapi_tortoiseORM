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
