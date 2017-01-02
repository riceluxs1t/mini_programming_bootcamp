import os

import errno
from django.core.management import BaseCommand
import boto3
import logging
from grader.config import HOMEWORK_NAME
from website.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_SUBMISSION_BUCKET_NAME

"""
A command that runs and creates a homework and its necessary directories
"""


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(HOMEWORK_NAME, type=str)

    def handle(self, *args, **options):
        homework_name = options.get(HOMEWORK_NAME)

        filename = "grader/submissions/" + homework_name + "/__init__.py"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, "w") as f:
            f.write("")
