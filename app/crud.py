# -*- coding: utf-8 -*-
"""
Database helper functions.
"""
from typing import Optional

from app.models.tortoise import Brewery


async def brewery(
    by_city: Optional[str] = None,
    by_type: Optional[str] = None,
    per_page: int = 20,
    page: int = 0,
) -> Optional[dict]:
    """
    Helper function for the app.beer.breweries endpoint.
    """
    return (
        Brewery.filter(
            city=by_city,
            brewery_type=by_type,
        )
        .limit(per_page)
        .offset(page)
    )


#   async def get_type(
#       brew_type: str, per_page: int = 50, page: int = 0
#   ) -> Optional[dict]:
#       """
#       Helper function for the app.beer.by_type endpoint.
#       """
#       the_type = (
#           await Brewery.filter(brewery_type=brew_type.lower())
#           .limit(50)
#           .offset(page)
#       )

#       if the_type:
#           return the_type
#       else:
#           return None
