
from django.core.management import BaseCommand

"""
A command that runs and downloads homework submissions from
the source control platform
"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        # TODO: impelment this feature


        import boto3
        s3_client = boto3.client('s3')
        s3_client.download_file(
            Bucket='rice-python-web-class',
                Key='homework/submission/',


            'rice-python-web-class', 'hello-remote.txt', 'hello2.txt')


