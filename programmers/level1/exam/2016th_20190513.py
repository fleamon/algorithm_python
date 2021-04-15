# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12901
"""
a	b	result
5	24	TUE
"""


import datetime


def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer


print solution(5, 24)
