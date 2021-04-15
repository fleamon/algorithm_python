#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3

input 에서 몇 쌍이 있는가?
"""

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#idx = 0   1   2   3   4   5   6   7   8
numAr = {}
res = 0

for idxAr in ar:
    # 있을때
    try:
        numAr[idxAr] = numAr[idxAr] + 1
        print numAr
    # 없을때
    except:
        numAr[idxAr] = 1
        print "--", numAr

print "====="
for idxNumAr in numAr:
    print numAr[idxNumAr]
    i = numAr[idxNumAr] / 2
    res = res + i
print "====="
#return res
print res


"""
from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ans = 0
    for val in [len(list(group)) for key, group in groupby(sorted(ar))]:
        ans = ans + val/2
    return ans
    """

