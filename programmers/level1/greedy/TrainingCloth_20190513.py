#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42862
"""
n	lost	reserve	    return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	        4
3	[3]	    [1]	        2
"""


def solution(n, lost, reserve):
    answer = [1] * n
    for i in reserve:
        answer[i-1] = 2
    for i in lost:
        answer[i-1] = answer[i-1]-1
    for index,value in enumerate(answer):
        if index > 0 and value == 0 and answer[index-1] == 2:
            answer[index] = 1
            answer[index-1] = 1
        elif (index == 0 or index < n-1) and value == 0 and answer[index+1] == 2:
            answer[index] = 1
            answer[index+1] = 1
    return n-answer.count(0)


print solution(5, [2, 4], [1, 3, 5])


"""
def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in lost:
        if i in reserve:
            answer = answer + 1
            reserve.remove(i)
        elif i - 1 in reserve:
            answer = answer + 1
            reserve.remove(i-1)
        elif i + 1 in reserve:
            answer = answer + 1
            reserve.remove(i+1)
        print lost
        print reserve
    return answer
"""

