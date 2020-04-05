#!/usr/bin/env python
# -*- encoding: utf-8

# https://www.acmicpc.net/problem/15997

"""
입력
KOREA CCC BBB AAA
KOREA CCC 1.0 0.0 0.0
AAA BBB 0.428 0.144 0.428
AAA KOREA 0.0 0.0 1.0
CCC BBB 0.0 0.0 1.0
KOREA BBB 1.0 0.0 0.0
CCC AAA 0.0 0.0 1.0

출력
1.0000000000
0.0000000000
0.5000000000
0.5000000000
"""

import operator

from numpy import rank

nations = list(raw_input().split())  # 국가 입력[0:3]
nationsPoint = {}
for i in nations:
    nationsPoint[i] = 0
perTable = []  # 2~7라인의 국가대항 퍼센트 적는 표 선언하고 입력
for i in range(0, 6):
    perTable.append(list(raw_input().split()))

# addPoint = {}  # 국가, 획득점수 저장
for i in perTable:
    maxValue = max(i[2:5])  # 최고확률
    maxCnt = i.count(max(i[2:5]))  # 최고확률 동률체크
    if maxValue == i[2] and maxCnt == 1:
        # 앞이 팀 이길 때
        nationsPoint[i[0]] = nationsPoint[i[0]] + 3
    elif (maxValue == i[3] and maxCnt == 1) or (maxValue != i[3] and maxCnt == 2):
        # 비길확률이 가장크거나, 이길확률==질확률일때
        nationsPoint[i[0]] = nationsPoint[i[0]] + 1
        nationsPoint[i[1]] = nationsPoint[i[1]] + 1
    else:
        # 뒤 팀이 이길 때
        nationsPoint[i[1]] = nationsPoint[i[1]] + 3

# print (nationsPoint)
### {'KOREA': 9, 'CCC': 0, 'BBB': 4, 'AAA': 4}
# print (sorted(nationsPoint.items(), key=operator.itemgetter(1), reverse=True))
### [('KOREA', 9), ('BBB', 4), ('AAA', 4), ('CCC', 0)]
sortNP = sorted(nationsPoint.items(), key=operator.itemgetter(1), reverse=True)
print (sortNP)

nationList = []
rankList = []
for i in sortNP:
    # print i
    nationList.append(i[0])
    rankList.append(i[1])
print nationList
print rankList
# print (sortNP[1])
# rankNP = rank(sortNP[1])


print rank(rankList)

