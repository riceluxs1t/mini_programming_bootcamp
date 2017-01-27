import math


def computeStandardDev(numbers):
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


def play369(numbers):
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


def findAllDeathTime(pos, vel, d):
    numAnts = len(pos)  # or len(vel)

    maxTime = -1

    for ant in range(numAnts):
        if vel[ant] > 0:
            maxTime = max(maxTime, d - pos[ant])
        else:
            maxTime = max(maxTime, pos[ant])
    return maxTime


def movingAverages(numbers, d):
    n = len(numbers)
    cumsum = [0] * (n + 1)
    for i in xrange(1, n + 1):
        cumsum[i] = cumsum[i - 1] + numbers[i - 1]

    moving_averages = []
    for i in xrange(d, n + 1):
        moving_averages.append((cumsum[i] - cumsum[i - d]) / float(d))

    return moving_averages


def robotopia(l1, a1, l2, a2, lt, at):

    is_done = 0
    ans = None
    for f_num in xrange(1, lt/l1 + 1):

        s_num = (lt - l1*f_num)/l2
        if f_num < 1 or s_num < 1:
            continue
        if (l1 * f_num + l2 * s_num) == lt and (a1 * f_num + a2 * s_num) == at:
            ans = (f_num, s_num)
            is_done += 1
            if is_done > 1:
                break

    if not ans or is_done > 1:
        return '?'
    else:
        return '{0} {1}'.format(ans[0], ans[1])
