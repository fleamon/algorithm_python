# -*- encoding: utf-8


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
answer = 0
for i in range(0, n):
    swapCnt = 0
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            answer = answer + 1
            swapCnt = swapCnt + 1
    if swapCnt == 0:
        break

print "Array is sorted in " + str(answer) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[len(a) - 1])

"""
3
1 2 3


Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
"""
