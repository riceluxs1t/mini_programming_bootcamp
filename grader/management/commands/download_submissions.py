import boto3
from django.core.management import BaseCommand

"""
A command that runs and downloads homework submissions from
the source control platform
"""


class Command(BaseCommand):
    # TODO : should create 'homework_name/user_name' dir with __init__.py then create homework_name.py with body from
    # TODO : each 'bucket/homework/user_name/homework_name'

    def handle(self, *args, **options):
        s3_client = boto3.resource('s3', aws_access_key_id="AKIAI5LREICCGFBFLJMQ",
                                 aws_secret_access_key="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")

        my_bucket = s3_client.Bucket('rice-python-web-class').get

        for object in my_bucket.objects.all():
            print(object)

        # s3_client.download_file(
        #     Bucket='rice-python-web-class',
        #     Key='/homework/hw.py',
        #     Filename = 'hw.py'
        # )


        # for bucket in s3.buckets.all():
        #     for key in bucket.objects.all():
        #         print(key.key)