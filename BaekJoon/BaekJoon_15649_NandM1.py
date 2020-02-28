#!/usr/bin/env python
# -*- encoding: utf-8

import itertools

N, M = map(int, raw_input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
tmpList = list(itertools.permutations(arr, M))
for i in tmpList:
    print " ".join(map(str, i))

"""
import itertools

N, M = map(int, raw_input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
tmpList = list(itertools.permutations(arr, M))
for i in tmpList:
    tmpArr = []
    for j in i:
        tmpArr.append(str(j))
    print " ".join(tmpArr)
"""
