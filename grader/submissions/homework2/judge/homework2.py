# -*- encoding:utf-8 -*-

import math

def help_jpago(original_sentence, list_of_pairs):

	translate_dictionary = {}

	for pair in list_of_pairs:
		translate_dictionary[pair[0]] = pari[1]

	# " " 기준으로 주어진 string 을 자름.
	words = original_sentence.split(" ")

	translated_sentence = ""

	for word in words:
		if word not in translate_dictionary:
			translated_sentence += word
			translated_sentence += " "
		else:
			translated_sentence += translate_dictionary[word]
			translated_sentence += " "

	# 마지막에 추가 된 " " 를 없앰.
	return translated_sentence.strip()


# O(n^2) version
def is_anagram_quadratic(s1, s2):

	if len(s1) != len(s2):
		return False

	chars = []
	for char in s1:
		chars.append(char)

	# remove matches!
	for char in s2:
		# this is O(n)
		chars.remove(char)

	if len(chars) == 0:
		return True
	return False

# O(nlogn) version
# sorting takes O(nlogn).
# http://stackoverflow.com/questions/4433915/why-is-sorting-a-string-on-log-n
def is_anagram_nlogn(s1, s2):
	s1.sort()
	s2.sort()

	return s1 == s2

def is_anagram(s1, s2):

	if len(s1) != len(s2):
		return False

	count1 = {}
	count2 = {}

	# count occurrences of each char in the first string
	for char in s1:
		if char not in count1:
			count1[char] = 0
		count1[char] = count1[char] + 1

	# count occurrences of each char in the second string
	for char in s2:
		if char not in count2:
			count2[char] = 0
		count2[char] = count2[char] + 1

	# for each character in the first string
	# check if it does not exist in the second string or the #s of occurrences differ
	# then, they are not anagrams
	for char in s1:
		if (char not in count2) or count2[char] != count1[char]:
			return False

	# otherwise, they are
	return True

# helper function used in the poker_chip_shuffle function.
def mixUp(l, r, isLeft):

    res = ''
    for idx in xrange(len(l)):
        if isLeft:
            res += l[idx]
            res += r[idx]
        else:
            res += r[idx]
            res += l[idx]

    return res

def poker_chip_shuffle(n, isLeft):
    r = 'r'*n
    b= 'b'*n
    cnt = 0

    while True:
        res = mixUp(r, b, isLeft)
        cnt += 1
        length = len(res)

        r = res[:length/2]
        b = res[length/2:]

        if (r == 'b'*n and b == 'r'*n) or (r == 'r'*n and b == 'b'*n):
            break

    return cnt

def poker_chip_shuffle_optimal(n):

	left_ans = poker_chip_shuffle(n, True)
	right_ans = poker_chip_shuffle(n, False)

	return min(left_ans, right_ans)


#######################################################
#######################################################
########### 몰라도 되는 exaustive search technique
###########
#######################################################
#######################################################

# dictionary but has default values for keys that don't exist
# uses the technique called the dynamic programming.
# i.e. don't ever compute values twice for the states you have seen already
# in other words, if have already seen the current left and right stacks more than once, you must have
# computed its value in the past. use it!
from collections import defaultdict
d = defaultdict(int)

# set is like a dictionary but specifically designed to support membership check operations quickly
# stores all the unique "states" seen so far.
has_seen = set([])

def poker_chip_shuffle_optimal_exahustive_sesarch(n, left, right, depth):

    # a base case state
    if ((left == 'r'*n and right == 'b'*n) or (left == 'b'*n and right =='r'*n)) and depth!=0:
        return 0

    # if already seen this state, use the cached value
    if d[(left, right)] != 0:
        return d[(left, right)]

    # if already seen this state but there is no value computed, return some large number 987654321 acts as our numerical choice of a positive infinity.
    if (left, right) in has_seen:
        return 987654321

    mixUpL = mixUp(left, right, True)
    mixUpR = mixUp(left, right, False)
    has_seen.add((left, right))

    # try both left and right first shuffles
    res1 = poker_chip_shuffle_optimal_exahustive_sesarch(n, mixUpL[:n], mixUpL[n:], depth+1)
    res2 = poker_chip_shuffle_optimal_exahustive_sesarch(n, mixUpR[:n], mixUpR[n:], depth+1)

    d[(left, right)] = min(res1, res2) + 1
    # return the minimum of the two.
    return min(res1, res2) + 1
