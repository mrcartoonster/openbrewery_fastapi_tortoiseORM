# -*- coding: utf-8 -*-
"""
Description for the docs and redocs page.
"""

desc = """
# OpenBreweryDB
---

FastAPI clone of [OpenBreweeryDB](https://www.openbrewerydb.org/). Using
[TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/index.html#) as the database backend.

If you find any benefit please sponsor me on GitHub


<iframe src="https://github.com/sponsors/mrcartoonster/button" title="Sponsor mrcartoonster" height="35" width="116" style="border: 0;"></iframe>
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
