# -*- coding: utf-8 -*-
# app/db.py
"""
Config for Orator ORM.
"""

from environs import Env
from orator import DatabaseManager, Model, Schema

env = Env()

env.read_env()


DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": env("db_name"),
        "user": env("db_user"),
        "password": env("db_password"),
        "prefix": "",
        "port": 5432,
    },
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
