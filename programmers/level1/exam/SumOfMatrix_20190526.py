# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12950
"""
arr1	            arr2	            return
[[1,2],[2,3]]	    [[3,4],[5,6]]	    [[4,6],[7,9]]
[[1],[2]]	        [[3],[4]]	        [[4],[6]]
"""


def solution(arr1, arr2):
    answer = arr1
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer


print solution([[1, 2],[2, 3]], [[3, 4],[5, 6]])
print solution([[1], [2]], [[3], [4]])

