# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12947
"""
arr	return
10	true
12	true
11	false
13	false
"""


def solution(x):
    strX = str(x)
    divisor = 0
    for i in strX:
        divisor = divisor + int(i)
    if x % divisor == 0:
        answer = True
    else:
        answer = False
    return answer


print solution(10)
print solution(12)
print solution(11)
print solution(13)
