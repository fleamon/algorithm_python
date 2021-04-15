# -*- encoding: utf-8


import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    res = 1
    while True:
        res = res * n
        n = n - 1
        if n == 0:
            break
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
