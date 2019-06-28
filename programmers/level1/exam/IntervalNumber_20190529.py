#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12954
"""
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
"""


def solution(x, n):
    answer = []
    tmp = x
    for i in range(0, n):
        answer.append(tmp)
        tmp = tmp + x
    return answer


print solution(2, 5)
print solution(4, 3)
print solution(-4, 2)
