from __future__ import unicode_literals

from django.apps import AppConfig

from website.settings import BASE_DIR


class GraderConfig(AppConfig):
    __name = 'grader'
    __grader_name = 'nk15'
    __base_dir = '/'.join([BASE_DIR, __name])
    __submission_dir = '/'.join([__base_dir, "submissions"])
    __grader_dir = '/'.join([__base_dir, "graders"])
    __grade_dir = '/'.join([__base_dir, "grades"])

    def get_grader_name(self):
        return self.__grader_name

    def get_submission_dir(self):
        return self.__submission_dir

    def get_graders_dir(self):
        return self.__grader_dir

    def get_grades_dir(self):
        return self.__grade_dir
