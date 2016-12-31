from base_grader import BaseGrader
from grader.models import Homework
from grader.config import DIR_SOLUTION


class Grader(BaseGrader):
    def __init__(self, *modules):
        super(Grader, self).__init__()
        (module, ) = modules
        self.expectedFunctions = Homework.objects.get(id=2).functions.split(',')

        self.assert_functions_exist(module, *self.expectedFunctions)

        # TODO: this attr injection method is probably not ideal

        for function_name in self.expectedFunctions:
            setattr(self, function_name, getattr(module, function_name))

        self.judge_data_dir = "/".join([DIR_SOLUTION, "judge_data", "homework2"])

    def get_test_file_path(self, file_name):
        return "/".join([self.judge_data_dir, file_name])

    def test_zigZag(self):
        with open(self.get_test_file_path("zigZag.in"), "r") as f_input, \
                open(self.get_test_file_path("zigZag.ans"), "r") as f_output:

            input = f_input.readline()
            output = "\n".join(f_output.readlines())

            passed_cases = 0

            passed_cases += self.test(output, self.zigZag, int(input))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, 1, "zigZag")


    def test_check_for_three(self):
        with open(self.get_test_file_path("check_for_three.in"), "r") as f_input, \
                open(self.get_test_file_path("check_for_three.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip().split(), self.check_for_three, *(map(int, input_line.strip().split())))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "check_for_three")

    def test_memory_cleaner(self):
        with open(self.get_test_file_path("check_for_three.in"), "r") as f_input, \
                open(self.get_test_file_path("check_for_three.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip().split(), self.check_for_three, *(map(int, input_line.strip().split())))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "check_for_three")
