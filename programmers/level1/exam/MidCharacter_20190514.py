#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12903
"""
s	    return
abcde	c
qwer	we
"""


def solution(s):
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    return answer


print solution("abcde")
print solution("qwer")
