#!/usr/bin/env python
#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input 0
7
0 0 1 0 0 1 0

Sample Output 0
4


Sample Input 1
6
0 0 0 0 1 0

Sample Output 1
3

2계단씩 올라갈 수 있지만 1은 밟으면 안됨
"""

n = 7
c = [0, 0, 1, 0, 0, 1, 0]
idxC = 0
res = 0

while 1:
    if idxC + 2 >= n:
        if idxC + 1 >= n:
            break
        else:
            if c[idxC+1] == 0:
                res = res + 1
                break

    else:
        if c[idxC+2] == 0:
            idxC = idxC + 2
            res = res + 1
        else:
            idxC = idxC + 1
            res = res + 1

print res
#return res


"""
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
"""



