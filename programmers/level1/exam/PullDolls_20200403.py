#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/64061

"""
board
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves
[1,5,3,5,1,2,1,4]
result
4

board
0,0,0,0,0
0,0,1,0,3
0,2,5,0,1
4,2,4,4,2
3,5,1,3,1
moves
1,5,3,5,1,2,1,4

쌓인 것
4,3,1,1,3,2,4
"""


def solution(board, moves):
    answer = 0
    tmpList = []
    for m in moves:
        for i in range(0, len(board)):
            if board[i][m-1] != 0:
                tmpList.append(board[i][m-1])
                board[i][m-1] = 0
                if len(tmpList) > 1:
                    if tmpList[len(tmpList)-1] == tmpList[len(tmpList)-2]:
                        tmpList.pop();tmpList.pop()
                        answer = answer + 2
                break
    return answer


print solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

