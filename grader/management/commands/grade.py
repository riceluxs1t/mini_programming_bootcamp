from datetime import date

from django.core.management.base import BaseCommand
from django.db.models import ObjectDoesNotExist

from grader.config import DIR_PYTHON_MODULE_SOLUTIONS, DIR_PYTHON_MODULE_SUBMISSIONS, DIR_GRADED_FILE, \
    HOMEWORK_NAME, USER_NAME
from homeworks.models import Homework


"""
A command that runs and grades homework submissions

i.e. python manage.py grade homework0 nate
"""


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(HOMEWORK_NAME, type=str)
        parser.add_argument(USER_NAME, type=str)

    def handle(self, *args, **options):

        homework_name = options.get(HOMEWORK_NAME)
        user_name = options.get(USER_NAME)

        if not homework_name or not user_name:
            return "You must supply the homework name and user name. i.e. python manage.py homework2 nate"

        print "Grading {0} for user {1} ... ".format(homework_name, user_name)

        # checks if the solution module exists
        try:
            grader = __import__(DIR_PYTHON_MODULE_SOLUTIONS % homework_name, fromlist=['solutions'])
        except ImportError as e:
            print e
            return "The test cases must be set up for grading %s! try again later" % homework_name

        modules = []

        # refers to the Homework model and get all the expected modules from the student submission directory
        try:
            homework = Homework.objects.get(homework_name=homework_name)
            for function in homework.modules.split(','):
                modules.append(
                    __import__(DIR_PYTHON_MODULE_SUBMISSIONS % (homework_name, user_name, function), fromlist=['submissions'])
                )
            # run the test cases.
            score = grader.Grader(homework_name, *modules).run_tests()
            self.write_grade(homework_name, user_name, score)

        except ObjectDoesNotExist:
            return "The corresponding project does not seem registered in the systems' Homework Model yet"

        except ImportError as e:
            print e
            return "Maybe a wrong file submitted"

        except SyntaxError as e:
            print e
            return "Some syntax in the submitted file? or an error in the judge system"

    # write the grade to the grade directory.
    def write_grade(self, project_name, user_name, score):
        with open(DIR_GRADED_FILE % (project_name, user_name), 'a+') as gradeFile:
            gradeFile.write("%s\t%s\t%s\n" % (user_name, score, date.today()))
