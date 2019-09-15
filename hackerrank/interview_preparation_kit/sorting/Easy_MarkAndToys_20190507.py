#!/usr/bin/env python
# -*- encoding: utf-8

# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

import os


# Complete the maximumToys function below.
def maximumToys(prices, k):
    res = 0
    wallet = 0
    prices = sorted(prices)
    for p in prices:
        wallet = wallet + p
        if wallet <= k:
            res = res + 1
    # return res
    print res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = raw_input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # prices = map(int, raw_input().rstrip().split())
    prices = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    result = maximumToys(prices, k)
    # fptr.write(str(result) + '\n')
    # fptr.close()
