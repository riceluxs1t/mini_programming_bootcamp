from base_grader import BaseGrader
from grader.models import Homework


class Grader(BaseGrader):
    def __init__(self, *modules):
        super(Grader, self).__init__()
        (module, ) = modules
        self.expectedFunctions = Homework.objects.get(id=2).functions.split(',')

        self.assert_functions_exist(module, *self.expectedFunctions)

        # TODO: this attr injection method is probably not ideal

        for function_name in self.expectedFunctions:
            setattr(self, function_name, getattr(module, function_name))

    def test_check_for_three_1(self):
        self.test(["T"], self.check_for_three, [3])

    def test_check_for_three_2(self):
        self.test(["T", "T", "F"], self.check_for_three, [3, 3, 6])

    # TODO: add more test cases here for homework2
