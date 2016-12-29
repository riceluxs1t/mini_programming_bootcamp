from grader.config import DIR_SOLUTION
from base_grader import BaseGrader
from grader.models import Homework

"""

A homework1 grader. An example of the grader that uses the outside judge data
with some extra I/O, which helps avoiding lots of boilerplat test case methods.

"""


class Grader(BaseGrader):
    def __init__(self, *modules):
        super(Grader, self).__init__()
        (module, ) = modules
        self.expectedFunctions = Homework.objects.get(id=1).functions.split(',')

        self.assert_functions_exist(module, *self.expectedFunctions)

        # TODO: this attr injection method is probably not ideal

        for function_name in self.expectedFunctions:
            setattr(self, function_name, getattr(module, function_name))

        self.judge_data_dir = "/".join([DIR_SOLUTION, "judge_data", "homework1"])

    def get_test_file_path(self, file_name):
        return "/".join([self.judge_data_dir, file_name])

    def run_judge_data(self, input_file_name, output_file_name, test_case_name):

        with open(self.get_test_file_path(input_file_name), "r") as f_input, \
                open(self.get_test_file_path(output_file_name), "r") as f_output:

            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip(), self.robotopia, *(map(int, input_line.strip().split())))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, test_case_name)

    def test_bad_inputs_one(self):
        self.run_judge_data("01_bad.in", "01_bad.ans", "test_bad_inputs_one")

    def test_bad_inputs_two(self):
        self.run_judge_data("02_bad.in", "02_bad.ans", "test_bad_inputs_two")

    def test_bad_inputs_three(self):
        self.run_judge_data("03_bad.in", "03_bad.ans", "test_bad_inputs_three")

    def test_large_inputs_one(self):
        self.run_judge_data("04_large_answers.in", "04_large_answers.ans", "test_large_inputs_one")

    def test_large_inputs_two(self):
        self.run_judge_data("05_large_answers.in", "05_large_answers.ans", "test_large_inputs_two")

    def test_large_inputs_three(self):
        self.run_judge_data("06_large_answers.in", "06_large_answers.ans", "test_large_inputs_three")

    def test_robotopia_secret_one(self):
        self.run_judge_data("07_robotopia_secret.in", "07_robotopia_secret.ans", "test_robotopia_secret_one")

    def test_robotopia_secret_two(self):
        self.run_judge_data("08_robotopia_secret.in", "08_robotopia_secret.ans", "test_robotopia_secret_two")

    def test_robotopia_secret_three(self):
        self.run_judge_data("09_robotopia_secret.in", "09_robotopia_secret.ans", "test_robotopia_secret_three")

    def test_robotopia_secret_four(self):
        self.run_judge_data("10_robotopia_secret.in", "10_robotopia_secret.ans", "test_robotopia_secret_four")

    def test_primes_one(self):
        self.run_judge_data("11_primes.in", "11_primes.ans", "test_primes_one")

    def test_primes_two(self):
        self.run_judge_data("12_primes.in", "12_primes.ans", "test_primes_two")

    def test_primes_three(self):
        self.run_judge_data("13_primes.in", "13_primes.ans", "test_primes_three")

    def test_hochberg_dependent_one(self):
        self.run_judge_data("hochberg_dependent-00.in", "hochberg_dependent-00.ans", "test_hochberg_dependent_one")

    def test_hochberg_dependent_two(self):
        self.run_judge_data("hochberg_dependent-01.in", "hochberg_dependent-01.ans", "test_hochberg_dependent_two")

    def test_hochberg_dependent_three(self):
        self.run_judge_data("hochberg_dependent-02.in", "hochberg_dependent-02.ans", "test_hochberg_dependent_three")

    def test_hochberg_independent_one(self):
        self.run_judge_data("hochberg_independent-00.in", "hochberg_independent-00.ans", "test_hochberg_independent_one")

    def test_hochberg_independent_two(self):
        self.run_judge_data("hochberg_independent-01.in", "hochberg_independent-01.ans", "test_hochberg_independent_two")

    def test_hochberg_independent_three(self):
        self.run_judge_data("hochberg_independent-02.in", "hochberg_independent-02.ans", "test_hochberg_independent_three")

