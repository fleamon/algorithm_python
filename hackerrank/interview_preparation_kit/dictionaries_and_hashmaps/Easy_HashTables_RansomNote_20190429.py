#!/usr/bin/env python
# -*- encoding: utf-8

import math
import os
import random
import re
import sys

from collections import Counter

"""
Sample Input 0
6 4
give me one grand today night
give one grand today

Sample Output 0
Yes


Sample Input 1
6 5
two times three is not four
two times two is four

Sample Output 1
No


Sample Input 2
7 4
ive got a lovely bunch of coconuts
ive got some coconuts

Sample Output 2
No


첫번째 라인의 첫번째 숫자 크기의 배열(두번째라인)과 첫번째 라인의 두번째 숫자 크기의 배열(세번째 라인)이 input되었을 때
세번째 라인의 모든 요소가 두번째 라인의 요소에 포함되는가?
"""
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print "Yes"
    else:
        print "No"


if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)


"""
def checkMagazine(magazine, note):
    noteCnt = len(note)                     # 6
    noteIdx = 0
    for idx in range(0, len(magazine)):     # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        if note[noteIdx] == magazine[idx]:
            noteIdx = noteIdx + 1           #
            if noteIdx == noteCnt:
                break
        else:
            continue
    if noteIdx == noteCnt:
        print "Yes"
    else:
        print "No"
    """


"""
def checkMagazine(magazine, note):
    mag = {}
    cnt = len(note)
    # input start!!!!!
    for mword in magazine:
        try:
            mag[mword] = mag[mword] + 1
        except:
            mag[mword] = 1
    # input end!!!!!
    for nword in note:
        try:
            if mag[nword] != 0:
                mag[nword] = mag[nword] - 1
                cnt = cnt - 1
            else:
                print "No"
                break
        except:
            print "No"
            break
    if cnt == 0:
        print "Yes"
        """

