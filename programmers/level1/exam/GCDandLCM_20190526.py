#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12940
"""
n	m	return
3	12	[3, 12]
2	5	[1, 10]
"""


def solution(n, m):
    answer = []
    nm = n * m
    while m != 0:
        tmp = n % m
        n = m
        m = tmp
    answer.append(abs(n))
    if int(answer[0]) == 0:
        answer.append(0)
    else:
        answer.append(nm / answer[0])
    return answer


print solution(3, 12)
print solution(2, 5)
