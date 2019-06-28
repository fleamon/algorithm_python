#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42578
"""
종류	    이름
얼굴	    동그란 안경, 검정 선글라스
상의	    파란색 티셔츠
하의	    청바지
겉옷	    긴 코트
"""


from collections import defaultdict


def solution(clothes):
    answer = 1
    clothCnt = defaultdict(int)
    for k, v in clothes:
        clothCnt[v] = clothCnt[v] + 1
    cntList = clothCnt.values()
    for i in cntList:
        answer = answer * (i + 1)
    return answer - 1


print '[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]'
print solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
print '[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]'
print solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
