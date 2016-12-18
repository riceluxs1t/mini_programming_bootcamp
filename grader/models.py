from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Homework(models.Model):

    homework_name = models.CharField()
    deadline = models.DateField()
    modules = models.CharField()  # comma separated list of modules names
