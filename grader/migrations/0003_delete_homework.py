# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0002_homework_functions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Homework',
        ),
    ]
