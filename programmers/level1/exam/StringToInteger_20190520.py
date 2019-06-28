#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12925
"""
str이 1234이면 1234를 반환하고, -1234이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
"""


def solution(s):
    if s[0] == "+":
        answer = int(s[1:])
    elif s[0] == "-":
        answer = int(s[1:]) * -1
    else:
        answer = int(s)
    return answer


print solution("1234")
print solution("-1234")
