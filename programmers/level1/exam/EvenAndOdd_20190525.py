# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12937
"""
num	    return
3	    Odd
4	    Even
"""


def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer


print solution(3)
print solution(4)
