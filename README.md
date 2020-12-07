![Beer](img/noun_Beer_23573.png)

![interrogate](img/interrogate_badge.svg) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# OpenBreweryDB Clone in FastAPI!
---

Welcome to my FastAPI clone of the cool [OpenBreweryDB](https://www.openbrewerydb.org/) API. This is my first FastAPI app that's been deployed into the wild. With that said, it's an MVP(Minimum Viable Product). It hasn't been fully tested in TDD and may fall apart due to it has yet to be ultimately stress tested. Currently stress testing it with the use of [Locust](https://locust.io/). If the app does fall apart, you're more than welcome to open an [issue](https://github.com/mrcartoonster/openbrewery_fastapi_tortoiseORM/issues) and I will respond letting you know when it's fixed.

Moreover, the *stack* used in this web app is again FastAPI with [TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/) handling the Postgres database. It will include Redis with the use of [FastAPI-cache](https://github.com/long2ice/fastapi-cache) extension in the next release to make this app more resilient and not fall apart or hang.

This app is hosted and deployed on Digital Ocean's [App Platform](https://www.digitalocean.com/docs/app-platform/). You're welcome to usethis project as a reference template to deploy. You know I am. If you do decide to deply on Digital Ocean, use my [link](https://m.do.co/c/beef14f5483f) to get \$100 for the fist 60 days! This app is also using [Fathom](https://usefathom.com/ref/QZWVPY), which is a GDPR, PECR and CCPA compliant Open Sourced Analytics framework. Really loving the breadth and simplicity of this software. If you want to keep your visitors infomation private and not track private information, try [Fathom](https://usefathom.com/ref/QZWVPY) out for free and use my [link](https://usefathom.com/ref/QZWVPY) to get \$10 off. Also, Fathom has a Digital Ocean Droplet ready to go. Again use my [Digital Ocean link](https://m.do.co/c/beef14f5483f) to get $100 credit for the first 60 days to try out that Fathom droplet.

If you haven't heard of `FastAPI`, it's a smooth Web Framework that's ...high performance, easy to learn, fast to code, ready for production. The [documetation](https://fastapi.tiangolo.com/) is expansive and you should be up and running with it in less than a day. I took a course on FastAPI via [TestDrivenIO](https://testdriven.io/courses/tdd-fastapi/?utm_source=mrcartoonster). TestDrivenIO's [FastAPI](https://testdriven.io/courses/tdd-fastapi/?utm_source=mrcartoonster) course will guide you on how to build a fully ML model with Docker practicing TDD and pushing up to Heroku with a GitHub Actions CI. This course has hidden Gems that I'll be using in my future FastAPI apps like [TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/), currently used in this app, and [NewsPaper3k](https://newspaper.readthedocs.io/en/latest/) for text summerization and scraping! If you're interested in TestDrivenIO's FastAPI course, you'll need to know a bit of FastAPI. If you can loop and know all the methods of a Python [dictionary](https://docs.python.org/3/library/stdtypes.html?highlight=dict#mapping-types-dict) you'll can cruise through the first three chapters of FastAPI documentation. Mainly the [Path Parameters]() section and [Query Paramters]() section. Or you can learn it in style with Calmcode.io's [FastAPI](https://calmcode.io/fastapi/hello-world.html) in less that half-n-hour.

I'm going to keep this app for two months to see the breaking points and to improve it. I'll be making my own FastAPI apps in the near future and this clone is just a test baloon. If you do find this useful and actually do use this API for day to day use, please donate in the following ways and I'll actually keep this app up and make it more resilient! You can donate by:

<iframe src="https://github.com/sponsors/mrcartoonster/button" title="Sponsor mrcartoonster" height="35" width="116" style="border: 0;"></iframe>
https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=73Q9EN2ZMWSVU&currency_code=USD
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="mrcartoontser" data-color="#FFDD00" data-emoji=""  data-font="Comic" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>

## My Socials
---

* You can catch me on Twitter at [@mrcartoonster](https://twitter.com/mrcartoonster)
* Instgram at [@pizzamachinegun](https://www.instagram.com/pizzamachinegun/)
* As well as email me at [mrcartoonster@fastmail.com](mrcartoonster@fastmail.com) for business inquiries.

## FastAPI Extensions
---

These are the FastAPI extensions used in thei app

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

This project keeps a [CHANGELOG](CHANGELOG.md)

Project Licensed under [New BSD License](LICENSE)
