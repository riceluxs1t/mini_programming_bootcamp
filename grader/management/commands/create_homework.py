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

        s3_client = boto3.client('s3', aws_access_key_id="AKIAI5LREICCGFBFLJMQ",
                                 aws_secret_access_key="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")

        # TODO : take python file dir as an arg and create python file in the bucket
        try:
            response = s3_client.put_object(
                Bucket='rice-python-web-class',
                Key='/homework/hw.py',
                Body=open('submission.py','rb')
                )
            logging.info("/homework/hw.py directory created  %s", response)
        except Exception as e:
            logging.warn("Bucket not there :: error %s", e)