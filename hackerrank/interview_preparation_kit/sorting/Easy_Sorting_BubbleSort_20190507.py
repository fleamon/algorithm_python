#!/usr/bin/env python
# -*- encoding: utf-8

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    cnt = 0
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
                cnt = cnt + 1
    print "Array is sorted in " + str(cnt) + " swaps."
    print "First Element: " + str(a[0])
    print "Last Element: " + str(a[len(a) - 1])

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
