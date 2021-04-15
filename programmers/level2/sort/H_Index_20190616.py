# -*- encoding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/42747

"""
citations	        return
[3, 0, 6, 1, 5]	    3
"""


def solution(citations):
    print citations
    citations.sort(reverse=True)
    print citations
    answer=[]
    for i in citations:
        cnt = 0
        for j in citations:
            if i <= j:
                # print i
                # print j
                cnt = cnt + 1
        # print "i   = " + str(i)
        # print "cnt = " + str(cnt)
        if i <= cnt:
            answer.append(i)
    return max(answer)


"""
def solution(citations):
    answer=[]
    citations.sort(reverse=True)
    for i in range(len(citations),0,-1):
        count=0
        for j in citations:
            if j >= i:
                count+=1
        if count <= i:
            answer.append(count)
        else:
            count=0
            answer.append(count)
    return max(answer)
"""
