import os
import re

from django.core.management import BaseCommand
from lectures.models import Lectures

"""
A command that runs and creates new Lectures django model instances for the corresponding
static/jupyter_lectures/lectureX.html files

i.e. for synchronization purposes

"""


class Command(BaseCommand):

    relative_path_to_lecture_html_files = "/static/jupyter_lectures/"
    regex_pattern_lecture_file = "^lecture[0-9]+\.html$"

    def handle(self, *args, **options):

        lecture_path = os.getcwd() + self.relative_path_to_lecture_html_files

        lectures = os.listdir(lecture_path)

        for lecture in lectures:

            if re.match(self.regex_pattern_lecture_file, lecture):

                lecture_number = int(lecture.split('.')[0].split('lecture')[1])
                if not Lectures.objects.filter(id=lecture_number).exists():
                    print "Creating a new Lectures django model instance for lecture {0}..".format(lecture_number)
                    Lectures.objects.create(id=lecture_number)
