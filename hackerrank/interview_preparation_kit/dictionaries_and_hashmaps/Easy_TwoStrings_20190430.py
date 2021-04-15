# -*- encoding: utf-8

import math
import os
import random
import re
import sys

from collections import Counter

"""
Sample Input
2
hello
world
hi
world

Sample Output
YES
NO


첫번째라인의 숫자개의 문자열 쌍이 input 되었을때(2~3라인, 3~4라인)
쌍의 첫번째 문자열과 두번째 문자열의 철자의 중복이 있는가? 
"""

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1dic = Counter(s1)
    s2dic = Counter(s2)
    tmp = s1dic - s2dic
    if s1dic != tmp:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
