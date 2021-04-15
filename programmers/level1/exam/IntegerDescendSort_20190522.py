# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12933
"""
n	    return
118372	873211
"""


def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    answer.sort(reverse=True)
    return int("".join(answer))


print solution(118372)

