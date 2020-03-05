#!/usr/bin/env python
# -*- encoding: utf-8

import sys

N, K = map(int, raw_input().split())
prefered = list(map(int, raw_input().split()))

min_std = float('inf')

while (K != (N + 1)):
    stride = 1
    full_range = ((N - K) // stride) + 1

    for i in range(full_range):
        do_list = prefered[i:(i + K)]
        mean = sum(do_list) / K
        var = sum([(x - mean) ** 2 for x in do_list]) / K
        std = var ** 0.5
        if (min_std >= std):
            min_std = std
    K += 1
sys.stdout.write(str(min_std))

"""
N, K = map(int, raw_input().split())
personNO = list(map(int, raw_input().split()))
minStd = float('inf')  # Minimum of standard deviation

while K != (N + 1):
    stride = 1
    fullRange = ((N - K) // stride) + 1

    for i in range(fullRange):
        doList = personNO[i:(i + K)]
        mean = sum(doList) / K
        var = sum([(x - mean) ** 2 for x in doList]) / K
        std = var ** 0.5  # standard deviation
        if minStd >= std:
            minStd = std
    K += 1

print str(minStd)
"""