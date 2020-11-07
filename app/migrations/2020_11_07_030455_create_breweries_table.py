# -*- coding: utf-8 -*-
"""
First migrations.
"""
from orator.migrations import Migration


class CreateBreweriesTable(Migration):
    """
    Simple migration.
    """

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("breweries") as table:
            table.increments("id")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("breweries")
