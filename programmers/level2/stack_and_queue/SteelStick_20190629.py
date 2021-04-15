# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42585

"""
arrangement	                return
()(((()())(())()))(())	    17
"""


def solution(arrangement):
    answer = 0
    cnt = 0
    for i in range(0, len(arrangement)):
        if arrangement[i] == "(":  # 막대기 시작 또는 레이져
            cnt = cnt + 1
        else:
            if arrangement[i - 1] == "(":  # 레이져
                cnt = cnt - 1
                answer = answer + cnt
            else:  # 막대기하나 끝
                cnt = cnt - 1
                answer = answer + 1
    return answer


print solution("()(((()())(())()))(())")


"""
def solution(arrangement):
    answer = 0
    cnt = 0
    for i in range(0, len(arrangement)):
        if arrangement[i] == "(":  # 막대기 시작 또는 레이져
            cnt = cnt + 1
        else:
            cnt = cnt - 1
            answer = answer + cnt
    return answer
"""
