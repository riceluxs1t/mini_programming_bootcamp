from datetime import date

from django.core.management.base import BaseCommand
from django.db.models import ObjectDoesNotExist
from grader.models import Homework

from grader.config import GRADE_DIR


"""
A command that runs and grades homework submissions
"""


class Command(BaseCommand):

    # option_list = BaseCommand.option_list + (
    #     make_option(
    #         '-h',
    #         '--homework',
    #         help='Type Homework name',
    #     ),
    #     make_option(
    #         '-n',
    #         '--user_name',
    #         help='Type user name',
    #     )
    # )

    def handle(self, *args, **options):
        # self.add_arguments(
        #     make_option(
        #         '-n',
        #         '--user_name',
        #         help='Type user name',
        #     )
        # )
        #
        # self.add_arguments(
        #     make_option(
        #         '-h',
        #         '--homework',
        #         help='Type Homework name',
        #     )
        # )
        # print dir(BaseCommand)
        # print args
        # homework_name, user_name = options['homework'], options['user_name']
        homework_name = 'test_grader'
        user_name = 'nate'
        grader = None

        print "Grading {0} for user {1} ... ".format(homework_name, user_name)

        try:
            grader = __import__("grader.solutions.%s" % homework_name, fromlist=['solutions'])
        except ImportError as e:
            print e
            print "The test cases must be set up for grading %s! try again later" % homework_name
            exit(-1)

        modules = []

        try:
            homework = Homework.objects.get(homework_name=homework_name)
            for module in homework.modules.split(','):
                modules.append(
                    __import__("grader.submissions.%s.%s.%s" % (homework_name, user_name, module), fromlist=['submissions'])
                )

            score = grader.Grader(*modules).run_tests()

            # TODO: add a dimension

            self.write_grade(homework_name, user_name, score)

        except ObjectDoesNotExist:
            print "The corresponding project does not seem registered in the systems' Homework Model yet"
            exit(-1)

        except ImportError as e:
            print e
            print "Maybe a wrong file submitted"

        except SyntaxError as e:
            print e
            print "Some syntax in the submitted file? or an error in the judge system"

    def write_grade(self, project_name, user_name, score):
        print GRADE_DIR
        with open('%s/%s-%s.txt' % (GRADE_DIR, project_name, user_name), 'a+') as gradeFile:
            gradeFile.write("%s\t%s\t%s\n" % (user_name, score, date.today()))
