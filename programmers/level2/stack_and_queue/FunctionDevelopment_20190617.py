#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42586

"""
progresses	    speeds	        return
[93,30,55]	    [1,30,5]	    [2,1]
"""


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(0, len(progresses)):
        day = 0
        while progresses[i] + (speeds[i] * day) < 100:
            day = day + 1
        days.append(day)
    sk = 0
    sv = days[0]
    for k, v in enumerate(days):
        if sv < v:
            answer.append(k-sk)
            sk = k
            sv = v
    answer.append(len(days)-sk)
    return answer


"""
def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        cnt = 0
        while progresses[0] <= 100:
            for i in range(0, len(progresses)):
                progresses[i] = progresses[i] + speeds[i]
        rmProList = []
        rmSpList = []
        for i in range(0, len(progresses)):
            if progresses[i] >= 100:
                cnt = cnt + 1
                rmProList.append(progresses[i])
                rmSpList.append(speeds[i])
        answer.append(cnt)
        for i in range(0, len(rmProList)):
            progresses.remove(rmProList[i])
            speeds.remove(rmSpList[i])
    return answer
"""


print solution([93, 30, 55], [1, 30, 5])
