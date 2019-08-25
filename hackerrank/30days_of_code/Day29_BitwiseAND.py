#!/usr/bin/end python
# -*- encoding: utf-8


def compare(n, k):
    if ((k-1) | k) <= n:
        print k-1
    else:
        print k-2

# Ver. 1 = 1 case timeout
"""
def compare(n, k):
    ansNomi = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i & j < k and i & j > ansNomi:
                ansNomi = i & j
    print ansNomi
"""

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        nk = raw_input().split()
        n = int(nk[0])
        k = int(nk[1])
        compare(n, k)

"""
3
5 2
8 5
2 2


1
4
0
"""
