import math
def computeStandardDev(numbers):
    total = 0
    total_= 0
    for number in numbers:
        total += number
    mean = (float(total)) / len(numbers)
    for number in numbers:
        total_ += (number - mean)**2
    total = total_/len(numbers)
    return math.sqrt(total)






def get_tens_ones(x):
    list1 = []
    list2 = []
    if ("3" in str(x)) or ("6" in str(x)) or ("9" in str(x)):	
        length = len(str(x))
        while length > 0:
            list1.append(x/(10**(length-1)))
            x -= (x/10**(length-1))* 10**(length-1)
            length -= 1
        for num in list1:
            if num == 3 or num ==6 or num == 9:
                list2.append("clap")
        return(list2)
    else:
        return str(x)

def play369(numbers):
    final_list = []
    for number in numbers:
        if len(str(number)) == 1:
            if (number == 3 or number == 6 or number ==9):
                final_list.append("clap")
            else:
                final_list.append(str(number))
        else:
            list = get_tens_ones(number)
            for i in list:
                final_list.append(i)
    return final_list




def findPair(numbers, x):
    i= 0
    j= len(numbers)-1
    list = []
    while j != i:
        if numbers[i] + numbers[j] > x:
            j-=1
        elif numbers[i] + numbers[j] < x:
            i+=1
        else:
            list.append([numbers[i],numbers[j]])
            i += 1
            j -= 1
    return list
                             



def movingAverages(numbers, d):
    sum = 0
    mean = 0
    list = []
    for i in range(d):
        sum += numbers[i]
    mean = sum/float(d)
    list.append(mean)
    for i in range(len(numbers)-d):
        mean =  (d * mean - numbers[i] + numbers[d+i])/d
        list.append(mean)
    return list
        

        
def findAllDeathTime(pos, vel, d):
    list = []
    max = 0
    for i in range(len(pos)):
        if vel[i] == 1:
            list.append(d-pos[i])
        else:
            list.append(pos[i])
    for j in list:
        if j > max:
            max = j
    return max

            

def robotopia(l1, a1, l2, a2, lt, at):
    if (float(l1*a2) - (a1 *l2)) == 0 or (a1 ==0):
        return "?"  
    robot1 = (float(at * l1) - (lt * a1)) / (float(l1*a2) - (a1 *l2))
    robot2 = (at-(float(a2)*robot1))/a1
    if (robot1 <1 or robot1 % 1.0 != 0):
        return "?"
    elif(robot2<1 or robot2 % 1.0 != 0):
        return "?"
    elif(l1 == 0 or a1 == 0 or l2 == 0 or a2 == 0):
        return "?"
    if (a1/float(a2)) == l1/(float(l2)):
        for (i) in float(range(len(lt +at))):
            if ((lt - l1*i)/ float(l2)) % 1.0 == 0:
                return [int(i),int((lt - l1*i)/ float(l2))]
        else:
            return "?"
    if robot1 % 1.0 == 0 and robot2 % 1.0 == 0.0:
        return [int(robot1),int(robot2)]
        
        
           
