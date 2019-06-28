#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12969
"""
입력
5 3

출력
*****
*****
*****
"""


# a, b = map(int, raw_input().strip().split(' '))
a, b = map(int, "5 3".strip().split(' '))
for i in range(0, b):
    tmp = ""
    for j in range(0, a):
        tmp = tmp + "*"
    print tmp

