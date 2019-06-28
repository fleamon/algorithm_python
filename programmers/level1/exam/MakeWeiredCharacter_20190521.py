#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12930
"""
s	                return
try hello world	    TrY HeLlO WoRlD
"""


def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        for k, v in enumerate(word):
            if k % 2 == 0:
                answer = answer + v.upper()
            else:
                answer = answer + v.lower()
        answer = answer + " "
    return answer[:-1]


print solution("try hello world")

