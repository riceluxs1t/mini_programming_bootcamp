import boto3
from grader.config import HOMEWORK_NAME, USER_NAME
from django.core.management import BaseCommand

"""
A command that runs and downloads homework submissions from
the source control platform
"""


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(HOMEWORK_NAME, type=str)
        parser.add_argument(USER_NAME, type=str)

    def handle(self, *args, **options):
        # TODO :
        homework_name = options.get(HOMEWORK_NAME)
        user_name = options.get(USER_NAME)

        s3_client = boto3.client('s3', aws_access_key_id="AKIAI5LREICCGFBFLJMQ",
                                 aws_secret_access_key="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")

        s3_client.download_file(
            Bucket='rice-python-web-class',
            Key='/homework/hw.py',
            Filename = 'hw.py'
        )


