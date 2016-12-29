import os

from django.test import TestCase

from config import DIR_MODULE_BASE, DIR_GRADE, DIR_SUBMISSION, DIR_SOLUTION


class TestConfig(TestCase):

    def test_check_directories_exist(self):
        try:
            os.listdir(DIR_MODULE_BASE)
        except OSError:
            self.fail("path {0} does not exist".format(DIR_MODULE_BASE))

        try:
            os.listdir(DIR_GRADE)
        except OSError:
            self.fail("path {0} does not exist".format(DIR_GRADE))

        try:
            os.listdir(DIR_SUBMISSION)
        except OSError:
            self.fail("path {0} does not exist".format(DIR_SUBMISSION))

        try:
            os.listdir(DIR_SOLUTION)
        except OSError:
            self.fail("path {0} does not exist".format(DIR_SOLUTION))


class TestGradeCommand(TestCase):

    def test_check_if_command_sanity_checks_work(self):
        pass