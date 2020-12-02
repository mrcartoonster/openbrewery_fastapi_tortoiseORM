# -*- coding: utf-8 -*-
"""
Envvars testing endpoint.
"""
# app/api/ping.py

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Settings view.
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
