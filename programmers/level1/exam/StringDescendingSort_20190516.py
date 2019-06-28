#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12917
"""
s	        return
Zbcdefg	    gfedcbZ
"""


def solution(s):
    answer = []
    for i in range(0, len(s)):
        answer.append(s[i])
    answer.sort(reverse=True)
    return "".join(answer)


print solution("Zbcdefg")
