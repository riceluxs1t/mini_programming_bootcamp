import sys
from datetime import date

from django.core.management import BaseCommand
from grader.models import Homework

from grader.config import GRADE_DIR


"""
A command that runs and grades homework submissions
"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        project_name, user_name = args[1], args[2]
        grader = None

        print "Grading {0} for user {1} ... ".format(project_name, user_name)

        try:
            grader = __import__("graders.%s" % project_name, fromlist=['graders'])
        except ImportError as e:
            print e
            print "The test cases must be set up for grading %s! try again later" % project_name
            exit(-1)

        modules = []

        homework = Homework.objects.filter(homework_name=project_name)

        if not homework.exists():
            print "The corresponding project does not seem registered in the systems' Homework Model yet"
            exit(-1)

        try:
            for module in homework.modules.split(','):
                modules.append(
                    __import__("submissions.%s.%s.%s" % (project_name, user_name, module), fromlist=['submissions'])
                )

            score = grader.Grader(*modules).run_tests()

            # TODO: add a dimension

            self.write_grade(project_name, user_name, score)

        except ImportError as e:
            print e
            print "Maybe a wrong file submitted"

        except SyntaxError as e:
            print e
            print "Some syntax in the submitted file? or an error in the judge system"

    def write_grade(self, project_name, user_name, score):
        with open('%s/%s-%s.txt' % (GRADE_DIR, project_name, user_name), 'a+') as gradeFile:
            gradeFile.write("%s\t%s\t%s\n" % (user_name, score, date.today()))
