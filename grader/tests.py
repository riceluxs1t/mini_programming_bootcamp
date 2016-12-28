import os

from django.test import TestCase

from config import MODULE_BASE_DIR, GRADE_DIR, SUBMISSION_DIR, SOLUTION_DIR


class TestConfig(TestCase):

    def test_check_directories_exist(self):
        try:
            os.listdir(MODULE_BASE_DIR)
        except OSError:
            self.fail("path {0} does not exist".format(MODULE_BASE_DIR))

        try:
            os.listdir(GRADE_DIR)
        except OSError:
            self.fail("path {0} does not exist".format(GRADE_DIR))

        try:
            os.listdir(SUBMISSION_DIR)
        except OSError:
            self.fail("path {0} does not exist".format(SUBMISSION_DIR))

        try:
            os.listdir(SOLUTION_DIR)
        except OSError:
            self.fail("path {0} does not exist".format(SOLUTION_DIR))


class TestGradeCommand(TestCase):

    def test_check_if_command_sanity_checks_work(self):
        pass