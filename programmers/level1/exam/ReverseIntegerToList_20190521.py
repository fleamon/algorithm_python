#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12932
"""
n	    return
12345	[5,4,3,2,1]
"""


def solution(n):
    answer = []
    for i in range (len(str(n)) - 1, -1, -1):
        answer.append(int(str(n)[i]))
    return answer


print solution(12345)

