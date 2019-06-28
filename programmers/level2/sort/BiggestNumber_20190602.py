#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42746

"""
numbers	                return
[6, 10, 2]	            6210
[3, 30, 34, 5, 9]	    9534330
"""


def solution(numbers):
    numbers = map(str, numbers)
    numbers.sort(cmp=lambda x, y: cmp(x+y, y+x), reverse=True)
    if int("".join(numbers)) == 0:
        return "0"
    else:
        return ''.join(numbers)


print solution([6, 10, 2])
print solution([3, 30, 34, 5, 9])


"""
from itertools import permutations

def solution(numbers):
    numArr = list(permutations(numbers, len(numbers))) # permutations
    answer = [] # save all permutations
    for i in range(0, len(numArr)):
        if numArr[i][0] == 0: # in each permutations, first parameter == 0: pass
            pass
        else:
            tmp = ''
            for j in range(0, len(numArr[i])):
                tmp = tmp + str(numArr[i][j])
            answer.append(tmp)
    return max(answer)
"""

"""
def solution(numbers):
    answer = []
    tmp = []
    for i in range(0, len(numbers)):
        tmp.append(str(numbers[i]))
    while len(tmp) > 1:
        if int(tmp[0]+tmp[1]) > int(tmp[1]+tmp[0]):
            answer.append(tmp[0])
            tmp.remove(tmp[0])
        else:
            answer.append(tmp[1])
            tmp.remove(tmp[1])
    answer.append(max(tmp))
    tmp.remove(max(tmp))
    return "".join(answer)
"""

"""
def solution(numbers):
    answer = []
    tmp = map(str, numbers)
    tmp.sort(reverse=True)
    while len(tmp) > 1:
        if int(tmp[0]+tmp[1]) > int(tmp[1]+tmp[0]):
            answer.append(tmp[0])
            tmp.remove(tmp[0])
        else:
            answer.append(tmp[1])
            tmp.remove(tmp[1])
    answer.append(tmp[0])
    tmp.remove(tmp[0])
    if int("".join(answer)) == 0:
        return "0"
    else:
        return "".join(answer)
"""

"""
def solution(numbers):
    numbers = map(str, numbers)
    numbers.sort(cmp=lambda x,y:cmp(x+y,y+x),reverse=True)
    if int("".join(numbers)) == 0:
        return "0"
    else:
        return ''.join(numbers)
"""
