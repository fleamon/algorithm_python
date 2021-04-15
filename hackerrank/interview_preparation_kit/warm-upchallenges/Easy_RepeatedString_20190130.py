#-*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input 0
aba
10

Sample Output 0
7

Sample Input 1
a
1000000000000

Sample Output 1
1000000000000

첫번째 input을 두번째 input 만큼 반복했을 때 a가 몇번 나오나!? 
"""
#s = "aba"
#n = 10
#s = "a"
#n = 1000000000000
s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
n = 736778906400
res = 0

"""
print s
print len(s)
print n / len(s)
print n % len(s)
print s[n % len(s)-1]
"""

s = s.strip()
quotient = n / len(s)
#print quotient
remainder = n % len(s)
#print remainder
#targetStr = s[remainder - 1]
targetStr = "a"
#print targetStr
res = s.count(targetStr)
#print res
res = res * quotient
#print res
for idxS in range (0, remainder):
    if s[idxS] == targetStr:
        res = res + 1
print res


"""
# Complete the repeatedString function below.
def repeatedString(s, n):
"""
