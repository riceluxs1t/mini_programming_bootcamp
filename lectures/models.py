from __future__ import unicode_literals

from django.db import models

"""
Model that represents each lecture
"""


class Lectures(models.Model):
    # TODO: add some other necessary fields.

    class Meta:
        db_table = "lectures"
