from __future__ import unicode_literals

from django.db import models

"""
Model that represents each lecture
"""


class Lectures(models.Model):

    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = "lectures"
