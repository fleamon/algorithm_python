#!/usr/bin/env python
# -*- encoding: utf-8

# Write your code here
class Calculator:
    def __init__(self):
        self.n = 0
        self.p = 0

    def power(self, n, p):
        if n < 0 or p < 0:
            return "n and p should be non-negative"
        else:
            return pow(n, p)


myCalculator = Calculator()
"""
4
3 5
2 4
-1 -2
-1 3
"""
T = int(raw_input())
for i in range(T):
    n, p = map(int, raw_input().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e

