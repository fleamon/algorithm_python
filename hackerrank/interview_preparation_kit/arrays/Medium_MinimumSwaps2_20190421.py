# -*- encoding: utf-8

"""
Sample Input 0
4
4 3 1 2

Sample Output 0
3


Sample Input 1
5
2 3 4 1 5

Sample Output 1
3


Sample Input 2
7
1 3 5 2 4 6 7

Sample Output 2
3

첫번째 input 개수크기의 배열이 숫자가 섞여서 들어왔을 때 순차적인 배열이 되려면 몇번 swap이 필요한가?
"""

def minimumSwaps(arr):
    res = 0
    idx = 0
    while idx < len(arr):
        if arr[idx] != (idx + 1):
            arr[arr[idx]-1], arr[idx] = arr[idx], arr[arr[idx]-1]
            res = res + 1
            continue
        idx = idx + 1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(raw_input())
    n = 4

    # arr = map(int, raw_input().rstrip().split())
    arr = [4, 3, 1, 2]

    print minimumSwaps(arr)

    # fptr.write(str(res) + '\n')

    # fptr.close()


"""
def minimumSwaps(arr):
    res = 0
    start = 1
    idx = 0
    tmp = 0
    l = len(arr)
    for i in range (idx, l):
        if arr[i] != start:
            tmp = arr[i]
            j = i + 1
            for j in range (idx + 1, l):
                if arr[j] == start:
                    arr[i] = arr[j]
                    arr[j] = tmp
                    res = res + 1
        start = start + 1
        idx = idx + 1
    return res
"""


"""
def minimumSwaps(arr):
    res = 0
    idx = 0
    while idx < len(arr):
        chk = arr.index(idx + 1)
        if chk == idx:
            idx = idx + 1
        else:
            tmp = arr[idx]
            arr[idx] = arr[chk]
            arr[chk] = tmp
            idx = idx + 1
            res = res + 1
    return res
"""
