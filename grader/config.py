from website.settings import BASE_DIR

EPSILON = 0.00000000001
MAX_NUM_SECONDS = 15

STRING_TIMEOUT = "Timed out!!"
STRING_ARG_FORMATTER = "when calling %s with "
STRING_NO_ARGUMENT = "no arguments."
STRING_WITH_ARGUMENT = "the argument %s"
STRING_INCORRECT_RETURN_VALUE = "got incorrect return value %s "
STRING_MODULE_HAS_NO_FUNCTION = "Submitted module %s does not have the required attribute %s"
STRING_PASSED_ALL_TEST_CASES = "You passed all test cases!"
STRING_FAILED_SOME_TEST_CASES = "You failed {0} test cases out all {1} test cases"
STRING_FAILED_TIME_OUT = "Error: function call timed out. You spent more than %d seconds " \
                         "in the function %r when called with arguments %r"


GRADER_NAME = "nk15"
MODULE_BASE_DIR = '/'.join([BASE_DIR, "graders"])
SUBMISSION_DIR =  '/'.join([MODULE_BASE_DIR, "submissions"])
GRADER_DIR = '/'.join([MODULE_BASE_DIR, "graders"])
GRADE_DIR = '/'.join([MODULE_BASE_DIR, "grades"])
