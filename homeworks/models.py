from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Homework(models.Model):

    is_visible = models.BooleanField(default=False)
    homework_name = models.CharField(max_length=30)
    deadline = models.DateField()
    modules = models.CharField(max_length=1000)  # comma separated list of modules names
    functions = models.CharField(max_length=1000)  # comma separated list of function names