#!/usr/bin/env python
# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42583
"""
경과 시간	    다리를 지난 트럭	    다리를 건너는 트럭	    대기 트럭
0	        []	                []	                [7,4,5,6]
1~2	        []	                [7]	                [4,5,6]
3	        [7]	                [4]	                [5,6]
4	        [7]	                [4,5]	            [6]
5	        [7,4]	            [5]	                [6]
6~7	        [7,4,5]	            [6]             	[]
8	        [7,4,5,6]	        []              	[]


bridge_length	    weight	    truck_weights	                    return
2	                10	        [7,4,5,6]	                        8
100	                100	        [10]	                            101
100	                100	        [10,10,10,10,10,10,10,10,10,10]	    110
"""


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    sec = 0
    while bridge:
        sec = sec + 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return sec


print solution(2, 10, [7, 4, 5, 6])
print solution(100, 100, [10])
print solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
