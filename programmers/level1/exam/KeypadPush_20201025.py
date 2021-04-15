# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    leftRow = 1; leftCol = 1
    rightRow = 1; rightCol = 3
    for number in numbers:
        if number in (1, 4, 7):
            if number == 1:
                leftRow = 4; leftCol = 1
            elif number == 4:
                leftRow = 3; leftCol = 1
            else: # 7
                leftRow = 2; leftCol = 1
            answer = answer + "L"
        elif number in (3, 6, 9):
            if number == 3:
                rightRow = 4; rightCol = 3
            elif number == 6:
                rightRow = 3; rightCol = 3
            else: # 9
                rightRow = 2; rightCol = 3
            answer = answer + "R"
        else: # 2, 5, 8, 0
            if number == 2:
                leftDistance = abs(leftRow - 4) + abs(leftCol- 2)
                rightDistance = abs(rightRow - 4) + abs(rightCol - 2)
                if leftDistance < rightDistance:
                    answer = answer + "L"
                    leftRow = 4; leftCol = 2
                elif leftDistance > rightDistance:
                    answer = answer + "R"
                    rightRow = 4; rightCol = 2
                else: # leftDistance == rightDistance
                    if hand == 'right':
                        answer = answer + "R"
                        rightRow = 4; rightCol = 2
                    else: # hand == 'left'
                        answer = answer + "L"
                        leftRow = 4; leftCol = 2
            elif number == 5:
                leftDistance = abs(leftRow - 3) + abs(leftCol- 2)
                rightDistance = abs(rightRow - 3) + abs(rightCol - 2)
                if leftDistance < rightDistance:
                    answer = answer + "L"
                    leftRow = 3; leftCol = 2
                elif leftDistance > rightDistance:
                    answer = answer + "R"
                    rightRow = 3; rightCol = 2
                else: # leftDistance == rightDistance
                    if hand == 'right':
                        answer = answer + "R"
                        rightRow = 3; rightCol = 2
                    else: # hand == 'left'
                        answer = answer + "L"
                        leftRow = 3; leftCol = 2
            elif number == 8:
                leftDistance = abs(leftRow - 2) + abs(leftCol- 2)
                rightDistance = abs(rightRow - 2) + abs(rightCol - 2)
                if leftDistance < rightDistance:
                    answer = answer + "L"
                    leftRow = 2; leftCol = 2
                elif leftDistance > rightDistance:
                    answer = answer + "R"
                    rightRow = 2; rightCol = 2
                else: # leftDistance == rightDistance
                    if hand == 'right':
                        answer = answer + "R"
                        rightRow = 2; rightCol = 2
                    else: # hand == 'left'
                        answer = answer + "L"
                        leftRow = 2; leftCol = 2
            else: # number == 0
                leftDistance = abs(leftRow - 1) + abs(leftCol- 2)
                rightDistance = abs(rightRow - 1) + abs(rightCol - 2)
                if leftDistance < rightDistance:
                    answer = answer + "L"
                    leftRow = 1; leftCol = 2
                elif leftDistance > rightDistance:
                    answer = answer + "R"
                    rightRow = 1; rightCol = 2
                else: # leftDistance == rightDistance
                    if hand == 'right':
                        answer = answer + "R"
                        rightRow = 1; rightCol = 2
                    else: # hand == 'left'
                        answer = answer + "L"
                        leftRow = 1; leftCol = 2
    return answer

"""
numbers	                            hand	    result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	    "LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	    "LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	    "LLRLLRLLRL"
"""

print solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
print solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")

print solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
print solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
print solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"
