from django.core.management import BaseCommand, call_command

from grader.config import HOMEWORK_NAME, USER_NAME


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        parser.add_argument(HOMEWORK_NAME, type=str)
        parser.add_argument(USER_NAME, type=str)

    def handle(self, *args, **options):
        output = call_command("grade", "homework1", "jh")
        return output
