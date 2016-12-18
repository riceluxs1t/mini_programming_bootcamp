import signal

from contextlib import contextmanager

from config import *


"""
Exception that gets triggered when a function times out.
"""


class TimeoutException(Exception):
    pass


"""
A context manager registered to trigger TimeOutException.
"""


@contextmanager
def context_manager_time_limit(seconds=MAX_NUM_SECONDS):
    def signal_handler(signum, frame):
        raise TimeoutException(STRING_TIMEOUT)

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


"""
A function that returns a informative formatted string with the function name and its arguments.
"""


def format_function_arguments(function_name, args):
    argument_string = STRING_ARG_FORMATTER % function_name

    if len(args) == 0:
        argument_string += STRING_NO_ARGUMENT
    elif len(args) == 1:
        argument_string += STRING_WITH_ARGUMENT % args[0]
    else:
        argument_string += STRING_WITH_ARGUMENT % (",".join([repr(x) for x in args]))

    return argument_string


"""
A function that returns a formatted string when the function returns a bad value.
"""


def format_wrong_return_value(actual, function_name, args):
    error = STRING_INCORRECT_RETURN_VALUE % actual
    return error + format_function_arguments(function_name, args)
