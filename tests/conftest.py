# -*- coding: utf-8 -*-
"""
Pytest fixtures and dummy data.
"""
from typing import Generator

import pytest


@pytest.fixture(scope="module")
def client() -> Generator:
    """
    Setup and Teardown of Tortoise.
    """
    pass
