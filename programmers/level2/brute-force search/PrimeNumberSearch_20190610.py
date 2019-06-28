#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42839
"""
numbers	    return
17	        3
011	        2
"""


from itertools import permutations


def solution(numbers):
    perList = []
    for i in range(1, len(numbers) + 1):
        perList = perList + list(permutations(numbers, i))
    numList = []
    for pers in perList:
        tmp = int("".join(pers))
        if tmp not in numList and tmp > 1:
            numList.append(tmp)

    rmList = []
    for i in numList:
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                rmList.append(i)
                break
    return len(numList) - len(rmList)


print solution("17")
print solution("011")


"""
from itertools import permutations
import math
  
limit = 9999999
eratos = [1] * (2 * limit + 1)
eratos[0] = 0 
eratos[1] = 1 
  
for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i): 
            eratos[j] = 0 
 
 
def solution(numbers):
    permutation_set = set([int("".join(item)) for i in range(7) for item in set(permutations(list(numbers), i + 1))]) 
    prime_list = [eratos[num] for num in permutation_set if num != 0 and num != 1]
 
    return sum(prime_list)
"""
