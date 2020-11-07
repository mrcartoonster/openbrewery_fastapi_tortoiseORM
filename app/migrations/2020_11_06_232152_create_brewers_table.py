# -*- coding: utf-8 -*-
"""
Migration to allready created table.
"""
from orator.migrations import Migration


class CreateBrewersTable(Migration):
    """
    Brewery table migrations.
    """

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("breweries") as table:
            """
            Brewery Table.
            """
            table.text("id").nullable()
            table.text("name").nullable()
            table.enum(
                "brewery_type",
                [
                    "closed",
                    "regional",
                    "micro",
                    "contract",
                    "brewpub",
                    "proprietor",
                    "bar",
                    "planning",
                    "large",
                ],
            ).nullable()
            table.text("street")
            table.text("address_2")
            table.text("address_3")
            table.text("city").nullable()
            table.text("state")
            table.text("country_province")
            table.text("postal_code").nullable()
            table.text("website_url")
            table.datetime("created_at")
            table.datetime("updated_at")
            table.text("country").nullable()
            table.decimal("longitude")
            table.decimal("latitude")
            table.boolean("tags").nullable()
            table.increments("idx")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("brewers")
