#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

2창원 배열이 input이 들어왔을 때 모래시계모양으로 있는 숫자를 더했을 때 최대값 구하기
"""

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
#arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0]] len=5

resArr = []
res = 0

#print arr[0]
#print len(arr)
#print arr[0][1]

for idxArr1 in range (0, 4):
    for idxArr2 in range (0, 4):
        #print arr[idxArr1][idxArr2]
        tmp = 0
        tmp = tmp\
              + arr[idxArr1][idxArr2] + arr[idxArr1][idxArr2 + 1] + arr[idxArr1][idxArr2 + 2]\
              + arr[idxArr1 + 1][idxArr2 + 1]\
              + arr[idxArr1 + 2][idxArr2] + arr[idxArr1 + 2][idxArr2 + 1] + arr[idxArr1 + 2][idxArr2 + 2]
        resArr.append(tmp)
#print resArr
res = max(resArr)

print res


"""
# Complete the hourglassSum function below.
def hourglassSum(arr):
"""
