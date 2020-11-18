# -*- coding: utf-8 -*-
"""
Settings and FastAPI test.

Remove once beer endpoints are registered.

"""
from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Setting test.
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
