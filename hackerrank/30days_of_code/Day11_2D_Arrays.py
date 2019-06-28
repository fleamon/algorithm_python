#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    res = []
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            tmp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] \
                  + arr[i + 1][j + 1] \
                  + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            res.append(tmp)

    print max(res)
