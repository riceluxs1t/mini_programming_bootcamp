import math
import random

from grader.config import DIR_SOLUTION
from base_grader import BaseGrader
from homeworks.models import Homework

"""

A homework1 grader. An example of the grader that uses the outside judge data
with some extra I/O, which helps avoiding lots of boilerplat test case methods.

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

        self.judge_data_dir = "/".join([DIR_SOLUTION, "judge_data", "homework1"])

    def get_test_file_path(self, file_name):
        return "/".join([self.judge_data_dir, file_name])

    def answer_computeStandardDev(self, numbers):
        sum_ = sum(numbers)
        numElements = len(numbers)

        # edge case.
        if numElements == 0:
            return 0

        mean_ = float(sum_) / numElements

        sum_of_differences = 0

        for number in numbers:
            sum_of_differences += (math.fabs(number - mean_)) ** 2

        return math.sqrt(sum_of_differences / numElements)

    def answer_play369(self, numbers):
        answer_sequence = []
        clap = "clap"
        condition = ["3", "6", "9"]

        for number in numbers:
            string_representation = str(number)

            isClap = False

            for char in string_representation:
                if char in condition:
                    answer_sequence.append(clap)
                    isClap = True
                    break

            if not isClap:
                answer_sequence.append(string_representation)

        return answer_sequence

    def answer_moving_average(self, numbers, d):
        n = len(numbers)
        cumsum = [0] * (n+1)
        for i in xrange(1, n + 1):
            cumsum[i] = cumsum[i-1] + numbers[i-1]

        moving_averages = []
        for i in xrange(d, n + 1):

            moving_averages.append((cumsum[i] - cumsum[i-d]) / float(d))

        return moving_averages

    def answer_ant_death_time(self, pos, vel, d):
        numAnts = len(pos)  # or len(vel)

        maxTime = -1

        for ant in range(numAnts):
            if vel[ant] > 0:
                maxTime = max(maxTime, d - pos[ant])
            else:
                maxTime = max(maxTime, pos[ant])
        return maxTime

    def run_judge_data(self, method_to_test, input_file_name, output_file_name, test_case_name):

        with open(self.get_test_file_path(input_file_name), "r") as f_input, \
                open(self.get_test_file_path(output_file_name), "r") as f_output:

            num_cases = f_input.readline()
            input_lines = f_input.readlines()
            output_lines = f_output.readlines()

            passed_cases = 0

            for input_line, output_line in zip(input_lines, output_lines):
                passed_cases += self.test(output_line.strip(), method_to_test, *(map(int, input_line.strip().split())))

            print "Passed {0} out of {1} cases for {2}".format(passed_cases, num_cases, test_case_name)

    def generate_random_std_input(self):
        num_ = random.randrange(1, 1000)
        input_list = []
        for _ in xrange(num_):
            input_list.append(random.randrange(1, 1000))
        return input_list


    def test_std_easy(self):
        for _ in xrange(1000):
            input_ = self.generate_random_std_input()
            self.test(self.answer_computeStandardDev(input_), self.computeStandardDev, input_, floatComparison=True)

    def test_std_tricky(self):
        input_ = [0]
        self.test(self.answer_computeStandardDev(input_), self.computeStandardDev, input_, floatComparison=True)

        input_ = [1]
        self.test(self.answer_computeStandardDev(input_), self.computeStandardDev, input_, floatComparison=True)

        input_ = [2] * 100
        self.test(self.answer_computeStandardDev(input_), self.computeStandardDev, input_, floatComparison=True)

    def test_369_easy(self):
        for _ in xrange(1000):
            input_ = range(1, random.randrange(1, 1000))
            self.test(self.answer_play369(input_), self.play369, input_)

    def test_moving_averages_simple(self):

        passed_cases = 0

        for testNum in xrange(1000):
            input_ = []
            for _ in xrange(1000):
                input_.append(random.randrange(1, 100))
            d = random.randrange(20, 70)

            passed_cases += self.test(self.answer_moving_average(input_, d), self.movingAverages, input_, d, tle=5)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 1000, 'test_moving_averages_simple')

    def test_moving_averages_hard_O_of_N(self):

        passed_cases = 0

        for testNum in xrange(50):
            input_ = []
            for _ in xrange(1000000):
                input_.append(random.randrange(5000, 10000))
            d = random.randrange(200000, 500000)

            passed_cases += self.test(self.answer_moving_average(input_, d), self.movingAverages, input_, d, tle=1)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 50, 'test_moving_averages_hard_O_of_N')

    def test_ant_easy_one_ant(self):

        passed_cases = 0

        for _ in xrange(1000):
            d = random.randrange(50, 1000)
            pos = [random.randrange(1, d-1)]
            vel = [1 if random.random() > 0.5 else -1]

            passed_cases += self.test(self.answer_ant_death_time(pos, vel, d), self.findAllDeathTime, pos, vel, d)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 1000, 'test_ant_easy_one_ant')

    def test_ant_easy_two_ants(self):

        passed_cases = 0

        for _ in xrange(1000):

            d = random.randrange(50, 1000)
            pos = [random.randrange(1, d/2), random.randrange(d/2 + 1, d - 1)]
            vel = [1 if random.random() > 0.5 else -1, 1 if random.random() > 0.5 else -1]
            passed_cases += self.test(self.answer_ant_death_time(pos, vel, d), self.findAllDeathTime, pos, vel, d)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 1000, 'test_ant_easy_two_ants')

    def test_ant_hard(self):

        passed_cases = 0

        for _ in xrange(50):
            d = random.randrange(5000, 10000)
            pos_set = set([])
            pos = []
            vel = []

            for idx in xrange(1000):
                x = random.randrange(1, d)
                if x not in pos_set:
                    pos_set.add(x)
                    pos.append(x)
                    vel.append(1 if random.random() > 0.5 else -1)

            passed_cases += self.test(self.answer_ant_death_time(pos, vel, d), self.findAllDeathTime, pos, vel, d, tle=1)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 50, 'test_ant_hard')

    def test_ant_hard2(self):

        passed_cases = 0

        for _ in xrange(50):
            d = random.randrange(500000, 1000000)
            pos_set = set([])
            pos = []
            vel = []

            for idx in xrange(10000):
                x = random.randrange(1, d)
                if x not in pos_set:
                    pos_set.add(x)
                    pos.append(x)
                    vel.append(1 if random.random() > 0.5 else -1)

            passed_cases += self.test(self.answer_ant_death_time(pos, vel, d), self.findAllDeathTime, pos, vel, d, tle=1)

        print "Passed {0} out of {1} cases for {2}".format(passed_cases, 50, 'test_ant_hard2')

    def test_bad_inputs_one(self):
        self.run_judge_data(self.robotopia, "01_bad.in", "01_bad.ans", "test_bad_inputs_one")

    def test_bad_inputs_two(self):
        self.run_judge_data(self.robotopia, "02_bad.in",  "02_bad.ans", "test_bad_inputs_two")

    def test_bad_inputs_three(self):
        self.run_judge_data(self.robotopia, "03_bad.in", "03_bad.ans", "test_bad_inputs_three")

    def test_large_inputs_one(self):
        self.run_judge_data(self.robotopia, "04_large_answers.in", "04_large_answers.ans", "test_large_inputs_one")

    def test_large_inputs_two(self):
        self.run_judge_data(self.robotopia, "05_large_answers.in", "05_large_answers.ans", "test_large_inputs_two")

    def test_large_inputs_three(self):
        self.run_judge_data(self.robotopia, "06_large_answers.in", "06_large_answers.ans", "test_large_inputs_three")

    def test_robotopia_secret_one(self):
        self.run_judge_data(self.robotopia, "07_robotopia_secret.in", "07_robotopia_secret.ans", "test_robotopia_secret_one")

    def test_robotopia_secret_two(self):
        self.run_judge_data(self.robotopia, "08_robotopia_secret.in", "08_robotopia_secret.ans", "test_robotopia_secret_two")

    def test_robotopia_secret_three(self):
        self.run_judge_data(self.robotopia, "09_robotopia_secret.in", "09_robotopia_secret.ans", "test_robotopia_secret_three")

    def test_robotopia_secret_four(self):
        self.run_judge_data(self.robotopia, "10_robotopia_secret.in", "10_robotopia_secret.ans", "test_robotopia_secret_four")

    def test_primes_one(self):
        self.run_judge_data(self.robotopia, "11_primes.in", "11_primes.ans", "test_primes_one")

    def test_primes_two(self):
        self.run_judge_data(self.robotopia, "12_primes.in", "12_primes.ans", "test_primes_two")

    def test_primes_three(self):
        self.run_judge_data(self.robotopia, "13_primes.in", "13_primes.ans", "test_primes_three")

    def test_hochberg_dependent_one(self):
        self.run_judge_data(self.robotopia, "hochberg_dependent-00.in", "hochberg_dependent-00.ans", "test_hochberg_dependent_one")

    def test_hochberg_dependent_two(self):
        self.run_judge_data(self.robotopia, "hochberg_dependent-01.in", "hochberg_dependent-01.ans", "test_hochberg_dependent_two")

    def test_hochberg_dependent_three(self):
        self.run_judge_data(self.robotopia, "hochberg_dependent-02.in", "hochberg_dependent-02.ans", "test_hochberg_dependent_three")

    def test_hochberg_independent_one(self):
        self.run_judge_data(self.robotopia, "hochberg_independent-00.in", "hochberg_independent-00.ans", "test_hochberg_independent_one")

    def test_hochberg_independent_two(self):
        self.run_judge_data(self.robotopia, "hochberg_independent-01.in", "hochberg_independent-01.ans", "test_hochberg_independent_two")

    def test_hochberg_independent_three(self):
        self.run_judge_data(self.robotopia, "hochberg_independent-02.in", "hochberg_independent-02.ans", "test_hochberg_independent_three")

