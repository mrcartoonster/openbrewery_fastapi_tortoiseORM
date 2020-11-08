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
            table.text("id")
            table.text("name")
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
            )
            table.text("street").nullable()
            table.text("address_2").nullable()
            table.text("address_3").nullable()
            table.text("city")
            table.text("state").nullable()
            table.text("country_province").nullable()
            table.text("postal_code")
            table.text("website_url").nullable()
            table.datetime("created_at").nullable()
            table.datetime("updated_at").nullable()
            table.text("country")
            table.decimal("longitude").nullable()
            table.decimal("latitude").nullable9
            table.boolean("tags").nullable()
            table.increments("idx")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("brewers")
