from website.settings import BASE_DIR

EPSILON = 0.00000000001
MAX_NUM_SECONDS = 15

# some grader module constant strings
STRING_TIMEOUT = "Timed out!!"
STRING_ARG_FORMATTER = "when calling %s with "
STRING_NO_ARGUMENT = "no arguments."
STRING_WITH_ARGUMENT = "the argument %s"
STRING_INCORRECT_RETURN_VALUE = "got incorrect return value %s "
STRING_MODULE_HAS_NO_FUNCTION = "Submitted module %s does not have the required attribute %s"
STRING_PASSED_ALL_TEST_CASES = "You passed all {0} test cases!"
STRING_FAILED_SOME_TEST_CASES = "You failed {0} test cases out all {1} test cases"
STRING_FAILED_TIME_OUT = "Error: function call timed out. You spent more than %d seconds " \
                         "in the function %r when called with arguments %r"

# some os specific path constants
GRADER_NAME = "nk15"
DIR_MODULE_BASE = '/'.join([BASE_DIR, "grader"])
DIR_SUBMISSION = '/'.join([DIR_MODULE_BASE, "submissions"])
DIR_SOLUTION = '/'.join([DIR_MODULE_BASE, "solutions"])
DIR_GRADE = '/'.join([DIR_MODULE_BASE, "grades"])

# some python style path constants
DIR_PYTHON_MODULE_SOLUTIONS = "grader.solutions.%s"
DIR_PYTHON_MODULE_SUBMISSIONS = "grader.submissions.%s.%s.%s"
DIR_GRADED_FILE = '/'.join([DIR_GRADE, "%s-%s.txt"])

# some named constants
HOMEWORK_NAME = "homework_name"
USER_NAME = "user_name"
TIMELIMIT = "time_limit"