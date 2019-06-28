#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42588
"""
송신 탑(높이)	    수신 탑(높이)
5(4)	        4(7)
4(7)	        2(9)
3(5)	        2(9)
2(9)	        -
1(6)	        -
"""


def solution(heights):
    answer = []
    tmp = []
    for i in range(len(heights) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                tmp.append(j + 1)
                break
            if j == 0:
                tmp.append(0)
    tmp.append(0)
    for i in range(len(tmp) - 1, -1, -1):
        answer.append(tmp[i])
    return answer


print solution([6, 9, 5, 7, 4])
