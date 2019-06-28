#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12919
"""
seoul	        return
[Jane, Kim]	    김서방은 1에 있다
"""


def solution(seoul):
    for k, v in enumerate(seoul):
        if v == "Kim":
            answer = "김서방은 %s에 있다" % k
    return answer


print solution(["Jane", "Kim"])
