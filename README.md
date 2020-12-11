![Beer](img/noun_Beer_23573.png)

![interrogate](img/interrogate_badge.svg) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# OpenBreweryDB Clone in FastAPI :beers:

Welcome to my FastAPI clone of the cool [OpenBreweryDB](https://www.openbrewerydb.org/) API. This is my first FastAPI app that's been deployed into the wild. With that said, it's an MVP(Minimum Viable Product). It hasn't been fully tested in TDD and may fall apart due to it has yet to be ultimately stress tested. Currently stress testing it with the use of [Locust](https://locust.io/). If the app does fall apart, you're more than welcome to open an [issue](https://github.com/mrcartoonster/openbrewery_fastapi_tortoiseORM/issues) and I will respond letting you know when it's fixed.

## FastAPI Extensions and Libraries ⚡️

Moreover, the *stack* used in this web app is again FastAPI with [TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/) handling the Postgres database asynchronusly. It uses [FastAPI-pagination](https://github.com/uriyyo/fastapi-pagination) for paging the app. The next future releases will include these amazing FastAPI extensions:

* [FastAPI-cache](https://github.com/long2ice/fastapi-cache) to make the app
  snappier by adding a Redis Cache to handle repeated requests.
* [FastAPI-versioning](https://github.com/DeanWay/fastapi-versioning) for
  simpler API versioning.
* [FastAPI-limiter](https://github.com/long2ice/fastapi-limiter) To limit requests to ease up on the database.

And maybe a couple more that will be listed here and in the
[CHANGELOG.md](CHANGELOG.md)

## Deployment 🚀

This app is hosted and deployed on Digital Ocean's [App Platform](https://www.digitalocean.com/docs/app-platform/). You're welcome to use this project as a reference template to deploy. You know I am. If you do decide to deply on Digital Ocean, use my [link](https://m.do.co/c/beef14f5483f) to get \$100 for the first 60 days!

## Analytics :chart_with_upwards_trend:

This app is also using [Fathom](https://usefathom.com/ref/QZWVPY), which is a GDPR, PECR and CCPA compliant Open Sourced Analytics framework. Really loving the breadth and simplicity of this software. If you want to keep your visitors infomation private and not track private information, try [Fathom](https://usefathom.com/ref/QZWVPY) out for free and use my [link](https://usefathom.com/ref/QZWVPY) to get \$10 off you first month. Also, Fathom has a Digital Ocean Droplet ready to go. Again use my [Digital Ocean link](https://m.do.co/c/beef14f5483f) to get $100 credit for the first 60 days to try out that Fathom droplet.

## Learn FastAPI Too 📝

If you haven't heard of `FastAPI`, it's a smooth Web Framework that's ...high performance, easy to learn, fast to code, ready for production. The [documetation](https://fastapi.tiangolo.com/) is expansive and you should be up and running with it in less than a day. I took a course on FastAPI via [TestDrivenIO](https://testdriven.io/courses/tdd-fastapi/?utm_source=mrcartoonster). TestDrivenIO's [FastAPI](https://testdriven.io/courses/tdd-fastapi/?utm_source=mrcartoonster) course will guide you on how to build a Restful-API ML model with Docker practicing TDD and pushing up to Heroku with a GitHub Actions CI. This course has hidden Gems that I'll be using in my future FastAPI apps like [TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/), currently used in this app, and [NewsPaper3k](https://newspaper.readthedocs.io/en/latest/) for text summerization and scraping! If you're interested in TestDrivenIO's FastAPI course, you'll need to know a bit of FastAPI. If you can loop and know all the methods of a Python [dictionary](https://docs.python.org/3/library/stdtypes.html?highlight=dict#mapping-types-dict) you can cruise through the first three sections of FastAPI documentation. Or you can learn it in style with Calmcode.io's [FastAPI](https://calmcode.io/fastapi/hello-world.html) free video course in less that half-n-hour.

## Plans for the app 🔖

I'm going to keep this app live for two months to see the breaking points and to improve it. It'll go down on 02/01/21. I'll be making my own FastAPI apps in the near future and this clone is just a test baloon. If you do find this useful and actually do use this API for day to day use, to keep it going please become a GitHub Sponsor by clicking the sponsor buttong to the right our:


## My Socials :speech_balloon:

* You can catch me on Twitter at [@mrcartoonster](https://twitter.com/mrcartoonster)
* Instgram at [@pizzamachinegun](https://www.instagram.com/pizzamachinegun/)
* As well as email me at [mrcartoonster@fastmail.com](mrcartoonster@fastmail.com) for business and job inquiries.

## Project Specifics

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

This project keeps a [CHANGELOG](CHANGELOG.md)

Project Licensed under [New BSD License](LICENSE)

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="mrcartoontser" data-color="#FF5F5F" data-emoji=""  data-font="Lato" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>
