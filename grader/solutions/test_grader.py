from base_grader import BaseGrader
from grader.models import Homework

"""
A test grader class

"""


class Grader(BaseGrader):
    def __init__(self, *modules):
        super(Grader, self).__init__()
        (module, ) = modules

        self.expectedModules = Homework.objects.get(id=0).modules.split(',')

        self.assert_functions_exist(module, *self.expectedModules)

        # TODO: this attr injection method is probably not ideal

        for function_name in self.expectedModules:
            setattr(self, function_name, getattr(module, function_name))

    def test_hello_world(self):
        self.test("hello world!", self.hello_world, "")

