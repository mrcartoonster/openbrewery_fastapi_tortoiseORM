# -*- coding: utf-8 -*-
"""
Description for the docs and redocs page.
"""

desc = r"""
# OpenCervezaDB
---

This is a [FastAPI](https://fastapi.tiangolo.com/) clone of the [OpenBreweryDB](https://www.openbrewerydb.org/).
You can read more about this project and ways to support by reading the
project's `README.md` in it's official [repository](https://github.com/mrcartoonster/openbrewery_fastapi_tortoiseORM)

If you find any value in this app and use it frequently, please consider
sponsoring the app to keep it going by clicking the GitHub Sponsor link below. Every bit helps!

Click here to go the OpenAPI docs to try this app out.

![GitHub Repo stars](https://img.shields.io/github/stars/mrcartoonster/openbrewery_fastapi_tortoiseORM?style=social?link=https://github.com/mrcartoonster/openbrewery_fastapi_tortoiseORM)
![GitHub issues](https://img.shields.io/github/issues/mrcartoonster/openbrewery_fastapi_tortoiseORM?style=social?link=https://github.com/mrcartoonster/openbrewery_fastapi_tortoiseORM/issues)
![GitHub Sponsors](https://img.shields.io/github/sponsors/mrcartoonster?style=social)

"""

brew_type = """
Filter by type of brewery.

Must be one of:
* `micro` - Most craft breweries. For example, Samual Adams is still considered a micro brewery.
* `nano` - An extremely small brewery which typically only distributes locally.
* `regional` - A regional location of an expanded brewery. Ex. Sierra Nevada's Asheville, NC location.
* `brewpub` - A beer-focused restaurant or restaurant/bar with a brewery on-premise.
* `large` - A very large brewery. Likely not for visitors. Ex. Miller-Coors. (deprecated)
* `planning` - A brewery in planning or not yet opened to the public.
* `bar` - A bar. No brewery equipment on premise. (deprecated)
* `contract` - A brewery that uses another brewery's equipment.
* `proprietor` - Similar to contract brewing but refers more to a brewery incubator.
* `close` - A location which has been closed.
"""


# logging fmt
fmt = (
    "<G>{level}</>:     <le>{message}</> "
    "<fg #3DDC2B>{time:YYYY.MM.DD at hh:mm:ss A zz}</>"
)
