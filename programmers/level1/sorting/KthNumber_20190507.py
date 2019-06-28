#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        arr = []
        for j in range(commands[i][0]-1, commands[i][1]):
            arr.append(array[j])
        arr.sort()
        answer.append(arr[commands[i][2]-1])
    return answer


print solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
