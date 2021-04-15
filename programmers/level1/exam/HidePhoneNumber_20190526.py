# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12948
"""
phone_number	    return
01033334444	        *******4444
027778888	        *****8888
"""


def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number[0:-4])):
        answer = answer + "*"
    answer = answer + phone_number[-4:]
    return answer


print solution("01033334444")
print solution("027778888")
