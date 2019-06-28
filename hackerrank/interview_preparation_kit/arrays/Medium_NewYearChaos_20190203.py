#!/usr/bin/env python
# -*- encoding: utf-8

import math
import os
import random
import re
import sys

"""
Sample Input
2
5
2 1 5 3 4
5
2 5 1 3 4

Sample Output
3
Too chaotic

input 첫줄 개수만큼의 짝수번째줄 input 크기의 3이상의 홀수 라인의 배열에 대해서 원래의 순차적 배열이 몇번의 원소 이동으로 만들어졌는가?
"""

def minimumBribes(q):
    res = 0
    # q : [2, 1, 5, 3, 4]
    # p : [1, 0, 4, 2, 3]
    # i : [0, 1, 2, 3, 4]
    #################
    # q : [2, 5, 1, 3, 4]
    # p : [1, 4, 0, 2, 3]
    # i : [0, 1, 2, 3, 4]
    for i, p in enumerate(q):
        p = p - 1
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p - 1, 0), i):
            if q[j] > p:
                res = res + 1
    print res

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
