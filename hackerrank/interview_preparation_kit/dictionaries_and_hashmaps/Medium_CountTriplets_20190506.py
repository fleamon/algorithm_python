# -*- encoding: utf-8

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    newC = Counter()
    existC = Counter()
    for i in arr:
        if i in existC:
            res = res + existC[i]
        if i in newC:
            existC[i * r] = existC[i * r] + newC[i]
        newC[i * r] = newC[i * r] + 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()


"""
def countTriplets(arr, r):
    res = 0
    tmpDic = Counter(arr)
    existArr = []
    for i in range(0, len(arr)-2):
        if arr[i] * r in tmpDic:
            if arr[i] * r * r in tmpDic:
                if r != 1:
                    if arr[i] not in existArr:
                        existArr.append(arr[i])
                        res = res \
                        + (tmpDic[arr[i]] * tmpDic[arr[i] * r] * tmpDic[arr[i] * r * r])
                else:
                    res = res + (len(list(combinations(arr, 3))) / (len(arr) - 2))
    return res
    """

"""
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    tmpDic = Counter(arr)
    existArr = []
    for i in range(0, len(arr)-2):
        if arr[i] * r in tmpDic:
            if arr[i] * r * r in tmpDic:
                if arr[i] not in existArr:
                    existArr.append(arr[i])
                    res = res \
                    + (tmpDic[arr[i]] * tmpDic[arr[i] * r] * tmpDic[arr[i] * r * r])
    return res
    """
