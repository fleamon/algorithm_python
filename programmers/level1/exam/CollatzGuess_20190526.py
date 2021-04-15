# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12943
"""
n	        result
6	        8
16	        4
626331	    -1
"""


def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        answer = answer + 1
        if answer > 500:
            answer = -1
            break
    return answer


print solution(6)
print solution(16)
print solution(626331)
