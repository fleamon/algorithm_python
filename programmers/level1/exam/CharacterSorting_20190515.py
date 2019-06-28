#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12915
"""
strings	            n	return
[sun, bed, car]	    1	[car, bed, sun]
[abce, abcd, cdx]	2	[abcd, abce, cdx]
"""


def solution(strings, n):
    answer = []
    for i in range(0, len(strings)):
        answer.append(strings[i][n] + strings[i])
    answer.sort()
    for i in range(0, len(answer)):
        answer[i] = answer[i][1:]
    return answer


print solution(['sun', 'bed', 'car'], 1)
print solution(['abce', 'abcd', 'cdx'], 2)
