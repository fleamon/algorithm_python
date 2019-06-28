#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42587
"""
priorities	            location	    return
[2, 1, 3, 2]	        2	            1
[1, 1, 9, 1, 1, 1]	    0	            5
"""


def solution(priorities, location):
    answer = 0
    priMod = [] # 나중에 location과 비교하려고 key, value로 만듦 (+2 라인)
    for i in range (0, len(priorities)):
        priMod.append([i, priorities[i]])
    i = 0
    cnt = 0
    while i != len(priMod):
        for j in range(i+1, len(priMod)):
            cnt = cnt + 1
            if priMod[i][1] < priMod[j][1]: # 뒤에 더 높은 우선순위가 있으면?
                priMod.append(priMod[i]) # 맨 앞을 맨뒤로 넣고 끝 (+2 라인)
                priMod.pop(i)
                break
        if cnt == (len(priMod) - (i+1)):
            cnt = 0
            i = i + 1
        else:
            cnt = 0
    for k, v in enumerate(priMod):
        if location == v[0]:
            answer = k + 1
    return answer


print solution([2, 1, 3, 2], 2)
print solution([1, 1, 9, 1, 1, 1], 0)
