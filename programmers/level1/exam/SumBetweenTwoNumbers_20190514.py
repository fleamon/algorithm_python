# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12912
"""
a	b	return
3	5	12
3	3	3
5	3	12
"""


def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b+1):
            answer = answer + i
    elif a > b:
        for i in range(b, a+1):
            answer = answer + i
    else:
        answer = a
    return answer


print solution(3, 5)
print solution(3, 3)
print solution(5, 3)
