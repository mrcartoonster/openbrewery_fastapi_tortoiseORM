# -*- coding: utf-8 -*-
# tests/unit/test_helpers.py
"""
Tests for Tortoise Helper function test.
"""
from app.api import crud


def test_by_city():
    """
    Test by_city helper function.
    """
    city = await crud.by_city("miami")

    assert "Miami" in city[0]
