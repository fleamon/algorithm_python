#!/usr/bin/env python
#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4

첫번째 input 개의 배열에서 두번째 input 번으로 배열을 왼쪽으로 이동
"""

"""
print a
for cnt in range (0, d):
    tmp = a[0]
    #print tmp
    for idxA in range(1, len(a)):
        a[idxA - 1] = a[idxA]
    a[len(a) - 1] = tmp
print a
"""

from collections import deque

a = [1, 2, 3, 4, 5]
d = 2
#print a
dArr = deque(a)
#print dArr
dArr.rotate(d * -1)
#print dArr
print list(dArr)


############################
##### NEW ANSWER START #####
#return a[d:] + a[:d]
###### NEW ANSWER END ######
############################


"""
# Complete the rotLeft function below.
def rotLeft(a, d):
"""
