#!/usr/bin/env python
# -*- encoding: utf-8

from itertools import combinations
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j in b]))
    return sum(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()


"""
def sherlockAndAnagrams(s):
    res = 0
    for n in range(1, len(s)):
        tmpArr = []
        for i in range(0, len(s)):
            if (i + n) < (len(s) + 1):
                tmpArr.append(s[i:i+n])
        midFinArr = []
        for idx in range(0, len(tmpArr)):
            midFinArr.append("".join(sorted(tmpArr[idx])))
        tmp = list(combinations(midFinArr, 2))
        for i in range(0, len(tmp)):
            if tmp[i][0] == tmp[i][1]:
                res = res + 1
    return res
"""

"""
def sherlockAndAnagrams(s):
    res = 0
    for n in range(1, len(s)):
        tmpArr = []
        for i in range(0, len(s)):
            if (i + n) < (len(s) + 1):
                tmpArr.append(s[i:i+n])
        midFinArr = []
        for idx in range(0, len(tmpArr)):
            midFinArr.append("".join(sorted(tmpArr[idx])))
        for i in range (0, len(midFinArr) - 1):
            for j in range (i + 1, len(midFinArr)):
                if midFinArr[i] == midFinArr[j]:
                    res = res + 1
    return res
"""

"""
def sherlockAndAnagrams(s):
    count = []
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j],2))) for j in b]))
    return sum(count)
    """

