#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12928
"""
n	return
12	28
5	6
"""


def solution(n):
    answer = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            answer = answer + i
    answer = answer + n
    return answer


print solution(12)
print solution(5)
