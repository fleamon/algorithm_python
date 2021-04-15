# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12934
"""
n	    return
121	    144
3	    -1
"""

import math


def solution(n):
    intTmp = int(math.sqrt(n))
    floatTmp = math.sqrt(n)
    if intTmp == floatTmp:
        answer = int(math.pow((intTmp + 1), 2))
    else:
        answer = -1
    return answer


print solution(121)
print solution(3)

