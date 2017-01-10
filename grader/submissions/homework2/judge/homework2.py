import copy
import math
import collections



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
            ret[i] = "F"
        else:
            ret[i] = "T"
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


# def isBalanced(str):
#     """
#     Check if the given string consisting of (,) is balanced. Search the definition of balanced.
#     Using stack or queue is recommended.
#     """
#     queue = collections.deque()
#     chars = list(str)
#     for i in chars:
#         if i == "(":
#             queue.append(1)
#         else:
#             if (len(queue) == 0):
#                 return "F"
#             else:
#                 queue.pop()
#
#     if len(queue) == 0:
#         return "T"
#     else:
#         return "F"
#
# def anagrams(string):
#     """
#     Find the number of substring pair that are anagrams to each other.
#     Using counter or dictionary is recommended.
#     """
#     count = 0
#     dict = {}
#     for i in range(0, len(string) + 1):
#         for j in range(i + 1, len(string) + 1):
#             chars = [x for x in list(string[i:j])]
#             chars.sort()
#             sorted = "".join(chars)
#             if sorted not in dict:
#                 dict[sorted] = 1
#             else:
#                 count += dict[sorted]
#                 dict[sorted] += 1
#     return count

