#!/usr/bin/env python
#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input
8
UDDDUDUU

Sample Output
1

Explanation
_/\      _
   \    /
    \/\/

시작높이를 지나가는 횟수 출력
"""
n = 8
s = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
res = 0
loc = 0
preloc = 0

for idxS in range (0, n):
    if s[idxS] == 'U':
        print 'U', idxS
        preloc = loc
        loc = loc + 1
        if preloc == 0 and loc < 0:
            res = res + 1
    elif s[idxS] == 'D':
        print 'D', idxS
        preloc = loc
        loc = loc - 1
        if preloc == 0 and loc < 0:
            res = res + 1

    print "loc : " + str(loc) + ", res : " + str(res) + ", preloc : " + str(preloc)

#return res
print res


"""
# Complete the countingValleys function below.
def countingValleys(n, s):
"""



