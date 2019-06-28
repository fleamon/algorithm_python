#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12944
"""
arr	        return
[1,2,3,4]	2.5
[5,5]	    5
"""


def solution(arr):
    s = 0
    for i in arr:
        s = s + i
    answer = s * 1.0 / len(arr)
    return answer


print solution([1, 2, 3, 4])
print solution([5, 5])
