# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12910
"""
arr	            divisor	    return
[5, 9, 7, 10]	5	        [5, 10]
[2, 36, 1, 3]	1	        [1, 2, 3, 36]
[3,2,6]	        10	        [-1]
"""


def solution(arr, divisor):
    answer = []
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer


print solution([5, 9, 7, 10], 5)
print solution([2, 36, 1, 3], 1)
print solution([3, 2, 6], 10)
