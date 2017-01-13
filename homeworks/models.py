from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Homework(models.Model):

    is_visible = models.BooleanField(default=False)
    homework_name = models.CharField(max_length=30)
    deadline = models.DateField()
    modules = models.CharField(max_length=1000)  # comma separated list of modules names
    functions = models.CharField(max_length=1000)  # comma separated list of function names


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10)  # student id uniquely associated with each django User.
    submission_key = models.CharField(max_length=50)  # key used to verify any submission for this user.
