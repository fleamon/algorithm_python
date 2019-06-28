#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42860
"""
name	    return
JEROEN	    56
JAN	        23
"""


def solution(name):
    answer = 0
    name = list(name)
    idx = 0
    while "".join(name) != ("A" * len(name)):
        ridx = 1
        lidx = 1
        if name[idx] != "A":
            if ord(name[idx]) == 78:
                answer = answer + 13
            elif ord(name[idx]) < 78:
                answer = answer + (ord(name[idx]) - 65)
            else:
                answer = answer + (91 - ord(name[idx]))
            name[idx] = "A"
        else:
            for i in range(1, len(name)):
                if name[idx + i] == "A":
                    ridx = ridx + 1
                else:
                    break
                if name[idx - i] == "A":
                    lidx = lidx + 1
                else:
                    break
            if ridx > lidx:
                answer = answer + lidx
                idx = idx - lidx
            else:
                answer = answer + ridx
                idx = idx + ridx
    return answer


print solution("JEROEN")
print solution("JAN")
