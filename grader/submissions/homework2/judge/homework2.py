import copy
import math
import collections


# HW2

# Q1
def zigZag(line):
    """
    Given an integer line, create a "line" lines of zigzag.
    Each line should contain 9 0s and 5 consecutive white spaces, switching the direction once it
    hits the wall. The white spaces starts from the left side of the string
    It should look something like this:
         #########
    #     ########
    ##     #######
    ###     ######
    ####     #####
    #####     ####
    ######     ###
    #######     ##
    ########     #
    #########
    #########
    ########     #
    #######     ##
    ...
    """
    string = ""
    toLeft = False
    for i in range(0, line):
        if i % 10 == 0:
            toLeft = not toLeft
        if toLeft:
            string += "#" * (i % 10) + " " * 5 + "#" * (9 - i % 10) + "\n"
        else:
            string += "#" * (9 - i % 10) + " " * 5 + "#" * (i % 10) + "\n"
    return string

print zigZag(1000)

def check_for_three(lst):
    """
    Given a list of integers,
    if the integer has 3 as a digit switch the entry to false, else true
    e.g)
    [1,2,13,3,5,6,33]
    will be turned into [T,T,F,F,T,T,F]
    """
    ret = copy.copy(lst)
    for i in range(0, len(lst)):
        if "3" in str(lst[i]):
            ret[i] = False
        else:
            ret[i] = True
    return ret


def memory_cleaner(lst):
    """
    Erase all repeated elements (not necessarily integers) in the list, leaving just one.
    Return the modified list.
    e.g)
    [1,1,1,1,2,2,3,3]
    will be turned into [1,2,3]
    """
    cache = set([])
    ret = copy.copy(lst)
    for i in lst:
        if i not in cache:
            cache.add(i)
        else:
            ret.remove(i)
    return ret


def same_sum_substring(string):
    """
    Given a string of consecutive integers that is in range [0,9].
    Find the number of substring pair that has an equal sum.
    Using dictionary or counter is recommended.
    """
    count = 0
    dict = {}
    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            ints = [int(x) for x in list(string[i:j])]
            subSum = sum(ints)
            if subSum not in dict:
                dict[subSum] = 1
            else:
                count += dict[subSum]
                dict[subSum] += 1
    return count


# HW3

def isBalanced(str):
    """
    Check if the given string consisting of (,) is balanced. Search the definition of balanced.
    Using stack or queue is recommended.
    """
    queue = collections.deque()
    chars = list(str)
    for i in chars:
        if i == "(":
            queue.append(1)
        else:
            if (len(queue) == 0):
                return False
            else:
                queue.pop()

    if len(queue) == 0:
        return True
    else:
        return False


def anagrams(string):
    """
    Find the number of substring pair that are anagrams to each other.
    Using counter or dictionary is recommended.
    """
    count = 0
    dict = {}
    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            chars = [x for x in list(string[i:j])]
            chars.sort()
            sorted = "".join(chars)
            if sorted not in dict:
                dict[sorted] = 1
            else:
                count += dict[sorted]
                dict[sorted] += 1
    return count

