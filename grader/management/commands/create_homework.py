from django.core.management import BaseCommand
import boto3
import logging
from grader.config import HOMEWORK_NAME, USER_NAME

"""
A command that runs and creates a homework and its necessary directories
"""


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(HOMEWORK_NAME, type=str)
        parser.add_argument(USER_NAME, type=str)

    def handle(self, *args, **options):
        homework_name = options.get(HOMEWORK_NAME)
        user_name = options.get(USER_NAME)

        s3_client = boto3.client('s3', aws_access_key_id="AKIAI5LREICCGFBFLJMQ",
                                 aws_secret_access_key="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")

        try:
            response = s3_client.put_object(
                Bucket='rice-python-web-class',
                Key='/homework/' + user_name +'/' + homework_name,
                Body=open('submission.py','rb') # TODO : specify how it will take in the python file
                )
            logging.info("/homework/hw.py directory created  %s", response)
        except Exception as e:
            logging.warn("Bucket not there :: error %s", e)