# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    answer = []
    ans1 = [1, 2, 3, 4, 5] * (len(answers) // len([1, 2, 3, 4, 5])) + [1, 2, 3, 4, 5][0:len(answers) % len([1, 2, 3, 4, 5])]
    cnt1 = 0
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // len([2, 1, 2, 3, 2, 4, 2, 5])) + \
           [2, 1, 2, 3, 2, 4, 2, 5][0:len(answers) % len([2, 1, 2, 3, 2, 4, 2, 5])]
    cnt2 = 0
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // len([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])) + \
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][0:len(answers) % len([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])]
    cnt3 = 0

    for i in range(0, len(answers)):
        if answers[i] == ans1[i]:
            cnt1 = cnt1 + 1
        if answers[i] == ans2[i]:
            cnt2 = cnt2 + 1
        if answers[i] == ans3[i]:
            cnt3 = cnt3 + 1

    cntArr = []
    cntArr.append(cnt1)
    cntArr.append(cnt2)
    cntArr.append(cnt3)
    m = max(cntArr)

    for i in range(0, len(cntArr)):
        if m == cntArr[i]:
            answer.append(i + 1)

    return answer


print solution([1, 2, 3])
print solution([1, 2, 3, 4, 5])
print solution([1, 3, 2, 4, 2])


"""
def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    # print 0 % 5
    for i in range(0, len(answers)):
        if i % 5 == 0:
            if answers[i] == 1:
                cnt1 = cnt1 + 1
        elif i % 5 == 1:
            if answers[i] == 2:
                cnt1 = cnt1 + 1
        elif i % 5 == 2:
            if answers[i] == 3:
                cnt1 = cnt1 + 1
        elif i % 5 == 3:
            if answers[i] == 4:
                cnt1 = cnt1 + 1
        elif i % 5 == 4:
            if answers[i] == 5:
                cnt1 = cnt1 + 1

        if i % 8 == 0:
            if answers[i] == 2:
                cnt2 = cnt2 + 1
        elif i % 8 == 1:
            if answers[i] == 1:
                cnt2 = cnt2 + 1
        elif i % 8 == 2:
            if answers[i] == 2:
                cnt2 = cnt2 + 1
        elif i % 8 == 3:
            if answers[i] == 3:
                cnt2 = cnt2 + 1
        elif i % 8 == 4:
            if answers[i] == 2:
                cnt2 = cnt2 + 1
        elif i % 8 == 5:
            if answers[i] == 4:
                cnt2 = cnt2 + 1
        elif i % 8 == 6:
            if answers[i] == 2:
                cnt2 = cnt2 + 1
        elif i % 8 == 7:
            if answers[i] == 5:
                cnt2 = cnt2 + 1

        if i % 10 == 0:
            if answers[i] == 3:
                cnt3 = cnt3 + 1
        elif i % 10 == 1:
            if answers[i] == 3:
                cnt3 = cnt3 + 1
        elif i % 10 == 2:
            if answers[i] == 1:
                cnt3 = cnt3 + 1
        elif i % 10 == 3:
            if answers[i] == 1:
                cnt3 = cnt3 + 1
        elif i % 10 == 4:
            if answers[i] == 2:
                cnt3 = cnt3 + 1
        elif i % 10 == 5:
            if answers[i] == 2:
                cnt3 = cnt3 + 1
        elif i % 10 == 6:
            if answers[i] == 4:
                cnt3 = cnt3 + 1
        elif i % 10 == 7:
            if answers[i] == 4:
                cnt3 = cnt3 + 1
        elif i % 10 == 8:
            if answers[i] == 5:
                cnt3 = cnt3 + 1
        elif i % 10 == 9:
            if answers[i] == 5:
                cnt3 = cnt3 + 1

    arr = []
    arr.append(cnt1)
    arr.append(cnt2)
    arr.append(cnt3)
    print arr
    m = max(arr)
    for i in range(0, len(arr)):
        if m == arr[i]:
            answer.append(i + 1)

    return answer
    """
