#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

import itertools

def solution(numbers):
    answer = []
    tmpList = list(itertools.combinations(numbers,2))
    for i in tmpList:
        if sum(list(i)) not in answer:
            answer.append(sum(list(i)))
    answer.sort()
    return answer

print solution([2,1,3,4,1]) # [2,3,4,5,6,7]
print solution([5,0,2,7]) # [2,5,7,9,12]