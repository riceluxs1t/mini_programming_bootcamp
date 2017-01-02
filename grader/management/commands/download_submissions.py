import os

import boto3
import errno
from django.core.management import BaseCommand

from grader.management.commands import create_homework
from website.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_SUBMISSION_BUCKET_NAME
from grader.config import USER_NAME, HOMEWORK_NAME

"""
A command that runs and downloads homework submissions from
the source control platform
"""


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(HOMEWORK_NAME, type=str)
        parser.add_argument(USER_NAME, type=str)


    def handle(self, *args, **options):
        s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        homework_name = options.get(HOMEWORK_NAME)
        user_name = options.get(USER_NAME)
        self.create_user_directory(homework_name, user_name)

        s3_client.download_file(
            Bucket=S3_SUBMISSION_BUCKET_NAME,
            Key='/' + user_name + '/' + homework_name + '/' + homework_name + ".py",
            Filename = 'grader/submissions/' + homework_name + '/' + user_name + '/' + homework_name + ".py"
        )

    def create_user_directory(self, homework_name, user_name):
        create_homework.create_file(homework_name)

        filename = "grader/submissions/" + homework_name + "/" + user_name + '/__init__.py'
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, "w") as f:
            f.write("")

