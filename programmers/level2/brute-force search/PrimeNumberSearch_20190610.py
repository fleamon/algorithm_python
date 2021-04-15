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








"""
수동

def solution(numbers):
    arr = []
    tmp = []
    for i in numbers:
        arr.append(i)
    visited = [False] * len(arr)
    num = []
    for i in range(1, len(arr) + 1):
        create(i, arr, 0, tmp, visited, num)

    num = list(set(num))
    m = max(num)
    # print confirm(num, m)
    return confirm(num, m)


def create(x, ar, depth, tmp, visited, num):
    if depth == x:
        x = ''.join(tmp)
        x = int(x)
        num.append(x)
        return

    for i in range(len(ar)):
        if not visited[i]:
            visited[i] = True
            tmp.append(ar[i])
            create(x, ar, depth+1, tmp, visited, num)
            visited[i] = False
            tmp.pop()


def confirm(array, n):
    list = [False, False] + [True] * (n - 1)
    index = []
    count = 0
    for i in range(2, n+1):
        if list[i]:
            index.append(i)
            for j in range(2*i, n+1, i):
                list[j] = False

    for i in array:
        for j in index:
            if i == j:
                count=count+1
                break

    return count
"""
