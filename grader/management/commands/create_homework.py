from django.core.management import BaseCommand


"""
A command that runs and creates a homework and its necessary directories
"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        :param args:
        :param options:
        :return: create hw directory to the bucket, and create python file
        """
        import boto3
        import logging

        s3_client = boto3.client('s3')

        try:
            response = s3_client.put_object(
                Bucket='rice-python-web-class',
                Key='homework/submission/hw.py')
            logging.info("  %s", response)
        except Exception as e:
            logging.warn("Bucket error %s", e)