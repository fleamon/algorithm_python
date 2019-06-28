#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12918
"""
s	    return
a234	false
1234	true
"""


def solution(s):
    answer = False
    cnt = 0
    if len(s) == 4 or len(s) == 6:
        for i in range (0, len(s)):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                cnt = cnt + 1
    if cnt == 4:
        answer = True
    return answer


print solution("a234")
print solution("1234")
