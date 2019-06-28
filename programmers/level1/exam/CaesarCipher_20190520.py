#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12926
"""
s	    n	result
AB	    1	BC
z	    1	a
a B z	4	e F d
"""


def solution(s, n):
    answer = ''
    # A 65    Z 90
    # a 97    z 122
    for i in s:
        if i == " ":
            answer = answer + " "
        else:
            if ord(i) >= 65 and ord(i) <= 90:
                if ord(i) + n > 90:
                    answer = answer + chr(ord(i) + n - 26)
                else:
                    answer = answer + chr(ord(i) + n)
            elif ord(i) >= 97 and ord(i) <= 122:
                if ord(i) + n > 122:
                    answer = answer + chr(ord(i) + n - 26)
                else:
                    answer = answer + chr(ord(i) + n)
    return answer


print solution("AB", 1)
print solution("z", 1)
print solution("a B z", 4)

