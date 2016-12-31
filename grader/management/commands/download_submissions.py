from boto3 import s3
from django.core.management import BaseCommand

import botocore



"""
A command that runs and downloads homework submissions from
the source control platform
"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        # TODO: impelment this feature
        bucket = s3.Bucket('mybucket')
        exists = True
        try:
            s3.meta.client.head_bucket(Bucket='mybucket')
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                exists = False
