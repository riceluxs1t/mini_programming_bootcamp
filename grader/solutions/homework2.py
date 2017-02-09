
from base_grader import BaseGrader
from grader.config import DIR_SOLUTION

from homeworks.models import Homework



class Grader(BaseGrader):
    def __init__(self, homework_name, *modules):
        super(Grader, self).__init__()
        (module, ) = modules

        self.expected_functions = Homework.objects.get(homework_name=homework_name).functions.split(',')

        self.assert_functions_exist(module, *self.expected_functions)


        # TODO: this attr injection method is probably not ideal

        for function_name in self.expected_functions:
            setattr(self, function_name, getattr(module, function_name))

        self.judge_data_dir = "/".join([DIR_SOLUTION, "judge_data", "homework2"])

    def get_test_file_path(self, file_name):
        return "/".join([self.judge_data_dir, file_name])


    def test_check_for_three(self):
        with open(self.get_test_file_path("check_for_three.in"), "r") as f_input, \
                open(self.get_test_file_path("check_for_three.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test([x for x in output_line.strip().split()], self.check_for_three, *([map(int, input_line.strip().split())]))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "check_for_three")

    def test_memory_cleaner(self):
        with open(self.get_test_file_path("memory_cleaner.in"), "r") as f_input, \
                open(self.get_test_file_path("memory_cleaner.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip().split(), self.memory_cleaner, *([input_line.strip().split()]))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "memory_cleaner")

    def test_same_sum_substring(self):
        with open(self.get_test_file_path("same_sum_substring.in"), "r") as f_input, \
                open(self.get_test_file_path("same_sum_substring.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(int(output_line.strip()), self.same_sum_substring, input_line.strip())

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "same_sum_substring")

    def test_isBalance(self):
        with open(self.get_test_file_path("isBalanced.in"), "r") as f_input, \
                open(self.get_test_file_path("isBalanced.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip(), self.isBalanced, input_line.strip())

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "isBalanced")

    def test_anagrams(self):
        with open(self.get_test_file_path("anagrams.in"), "r") as f_input, \
                open(self.get_test_file_path("anagrams.ans"), "r") as f_output:

            # Change from here
            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(int(output_line.strip()), self.anagrams, input_line.strip())

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, "anagrams")