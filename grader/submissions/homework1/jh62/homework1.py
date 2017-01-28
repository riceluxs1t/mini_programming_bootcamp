# 1
####################################################3
import math


def computeStandardDev(numbers):
    total = 0
    total_ = 0
    for number in numbers:
        total += number
    mean = float(total) / len(numbers)
    for number in numbers:
        total_ += (number - mean) ** 2
    total = total_ / len(numbers)
    return math.sqrt(total)


numb = [2, 4, 4, 4, 5, 5, 7, 9]
print computeStandardDev(numb)


#####################################################3
# 2

def get_tens_ones(x):
    list1 = []
    list2 = []
    if ("3" in str(x)) or ("6" in str(x)) or ("9" in str(x)):
        length = len(str(x))
        while length > 0:
            list1.append(x / (10 ** (length - 1)))
            x -= (x / 10 ** (length - 1)) * 10 ** (length - 1)
            length -= 1
        for num in list1:
            if num == 3 or num == 6 or num == 9:
                list2.append("clap")
        return list2
    else:
        return str(x)



#######################################################################
def play369(numbers):
    final_list = []
    for number in numbers:
        if len(str(number)) == 1:
            if (number == 3 or number == 6 or number == 9):
                final_list.append("clap")
            else:
                final_list.append(str(number))
        else:
            final_list.append(get_tens_ones(number))
    return final_list


###############################################################

def findPair(numbers, x):
    list = []
    for number1 in numbers:
        for number2 in numbers:
            if numbers.index(number1) < numbers.index(number2):
                if number1 + number2 == x:
                    list.append([number1, number2])
    return list


##################################################################

def movingAverages(numbers, d):
    sum = 0
    list = []
    for number in numbers:
        if numbers.index(number) + d < len(numbers) + 1:
            for i in range(d):
                sum += numbers[(numbers.index(number)) + i]

            list.append(float(sum) / d)
            sum = 0
    print len(numbers), len(list), d
    return list



#########################################################




def findAllDeathTime(pos, vel, d):
    max = 0
    list = []
    for number in range(len(pos)):
        if vel[number] == 1:
            pt = d - pos[number]
            list.append(pt)
        else:
            if pos[number] > d:
                return pos[number] - d
            else:
                return pos[number]
    for number in list:
        if number > max:
            max = number
    return number


########################################################

def robotopia(l1, a1, l2, a2, lt, at):
    leg = 0
    arm = 0
    leg = (float(lt * a2) - (at * l2)) / ((l1 * a2) - (a1 * l2))
    arm = (lt - (leg * l1)) / float(l2)
    if leg % 1.0 == 0.0 and arm % 1.0 == 0.0:
        return '{0} {1}'.format(int(leg), int(arm))
    else:
        return "?"