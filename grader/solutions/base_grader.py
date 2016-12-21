from grader.config import MAX_NUM_SECONDS, EPSILON, STRING_MODULE_HAS_NO_FUNCTION, STRING_PASSED_ALL_TEST_CASES, \
    STRING_FAILED_SOME_TEST_CASES, STRING_FAILED_TIME_OUT
from utility import context_manager_time_limit, format_function_arguments, format_wrong_return_value, TimeoutException


"""
All grader must subclass this base grader and run the "runTests" method.
"""


class BaseGrader(object):
    def __init__(self):
        self.failed_test_cases = []
        self.num_test_cases = len(self.get_test_cases())

    """
    asserts if the submitted .py file has all the functions to be implemented.
    """
    def assert_functions_exist(self, module, *function_names):

        for function_name in function_names:
            if not hasattr(module, function_name):
                # TODO: do it in more reliable way than this.
                module_name = m.__name__[m.__name__.rfind(".") + 1:]
                print STRING_MODULE_HAS_NO_FUNCTION % (module_name, function_name)
                exit(-1)

    """
    Grabs all the test cases defined in the subclass of base_grader.

    Looks for all the methods that have prefix "test". Excludes the "test" method.

    """
    def get_test_cases(self):
        return [attr for attr in dir(self) if attr != "test" and attr.startswith("test")]

    """
    Runs all the tests.
    """
    def run_tests(self):
        for test_case in self.get_test_cases():
            try:
                getattr(self, test_case)()
            except Exception as e:
                self.failed_test_cases.append("You caused a %s: %s " % (type(e).__name__, e))
                raise

        failed_test_cases = len(self.failed_test_cases)
        if failed_test_cases == 0:
            print STRING_PASSED_ALL_TEST_CASES
            return 1.0
        else:

            print STRING_FAILED_SOME_TEST_CASES.format(failed_test_cases, self.num_test_cases)

            # TODO: actually tell what cases they failed.

            return float(self.num_test_cases - failed_test_cases) / failed_test_cases

    """
    Runs a single test case.

    """
    def test(self, expected, function, *args, **kwargs):
        try:
            with context_manager_time_limit():
                actual = function(*args)

                if expected != actual and ('floatComparison' not in kwargs or abs(expected - actual) > EPSILON):
                    self.failed_test_cases.append(format_wrong_return_value(actual, function.__name__, args))

        except TimeoutException:
            self.failed_test_cases.append(
                STRING_FAILED_TIME_OUT % (MAX_NUM_SECONDS, function.__name__, args)
            )
        except Exception as e:
            self.failed_test_cases.append(
                "Error: %s " % e + format_function_arguments(function.__name__, args)
            )
