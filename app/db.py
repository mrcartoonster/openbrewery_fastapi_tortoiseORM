# -*- coding: utf-8 -*-
"""
Ormar metadata init.

Following the imports and initialization:
https://collerek.github.io/ormar/fastapi/#imports-and-initialization

"""
import databases
import ormar
import sqlalchemy
from environs import Env

env = Env()
env.read_env()

# Following the FastAPI in parts section of sql database ORM. This will be
# where our database is connected and initialized. We'll be imported in the
# main.py to actually be created
metadata = sqlalchemy.MetaData()
database = databases.Database(env("DEV_DB"))

# Using Ormar bestpractice to initialize the Meta class for the ormar model in
# one place. Following this execution from the tutorial
# https://collerek.github.io/ormar/models/#best-practice


class MainMeta(ormar.ModelMeta):
    """
    Quick Meta init with tablename.
    """

    metadata = metadata
    database = metadata
    tablename = "breweries"
