from base_grader import BaseGrader
from homeworks.models import Homework

"""
A test grader class

"""


class Grader(BaseGrader):
    def __init__(self, homework_name, *modules):
        super(Grader, self).__init__()
        (module, ) = modules

        self.expected_functions = Homework.objects.get(homework_name=homework_name).functions.split(',')

        self.assert_functions_exist(module, *self.expected_functions)

        # TODO: this attr injection method is probably not ideal

        for function_name in self.expected_functions:
            setattr(self, function_name, getattr(module, function_name))

    def test_hello_world(self):
        self.test("hello world!", self.hello_world, "")

