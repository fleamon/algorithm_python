# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42889
"""
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

입출력 예
N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4, 4, 4, 4, 4]	            [4,1,2,3]
"""


def solution(N, stages):
    answer = []
    arrive = {}
    cnt = 0
    for i in range(1, N+1):
        cnt = cnt + stages.count(i)
        print cnt
        print stages.count(i) * 1.0
        print len(stages) - cnt
        if len(stages) == cnt:
            arrive[i] = 1.0
        else:
            arrive[i] = (stages.count(i) * 1.0) / (len(stages) - cnt)
        print arrive
        print "="
        # arrive[i] = (stages.count(i) * 1.0) / (len(stages))
    sortArrive = sorted(arrive.items(), reverse = True, key = lambda arrive: arrive[1])
    print arrive
    print sortArrive
    for i in sortArrive:
        print i[0]
        answer.append(i[0])
    return answer


print solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print "===================================="
print "===================================="
print solution(4, [4, 4, 4, 4, 4])
