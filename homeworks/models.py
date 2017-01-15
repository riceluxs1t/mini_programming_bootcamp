from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from website.pbkdf2 import pbkdf2_check


class Homework(models.Model):

    is_visible = models.BooleanField(default=False)
    homework_name = models.CharField(max_length=30)
    deadline = models.DateField()
    modules = models.CharField(max_length=1000)  # comma separated list of modules names
    functions = models.CharField(max_length=1000)  # comma separated list of function names


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: postgresSQL behaves in a weird way..
    student_id = models.CharField(max_length=10, default="")  # student id uniquely associated with each django User.
    submission_key = models.CharField(max_length=255, default="")  # key used to verify any submission for this user.

    def check_password(self, password):
        return pbkdf2_check(password, self.submission_key)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
