#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12935
"""
arr	        return
[4,3,2,1]	[4,3,2]
[10]	    [-1]
"""


def solution(arr):
    arr.remove(min(arr))
    answer = []
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    return answer


print solution([4, 3, 2, 1])
print solution([10])

