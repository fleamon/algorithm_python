# -*- encoding: utf-8

"""
Sample Input
5 3
1 2 100
2 5 100
3 4 100

Sample Output
200

첫번째 라인의 첫번째 input 크기만큼의 배열에 두번째 input 값 만큼의 명령이 수행된다.
두번째 라인부터 첫번째라인의 두번째 input 개수가 시작되는데
첫전째 라인의 첫번째 input 번째부터 두번째 input 번째까지 세번째 값을 더하면 최종적으로 배열에서 가장 큰 수는?
"""

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    print arr
    for first, last, val in queries:
        arr[first-1] = arr[first-1] + val
        arr[last] = arr[last] - val
        print arr
    res = 0
    tmp = 0
    for i in arr:
        tmp = tmp + i
        if tmp > res:
            res = tmp
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = raw_input().split()

    # n = int(nm[0])
    n = 5
    # m = int(nm[1])

    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    print arrayManipulation(n, queries)

    # for _ in xrange(m):
    #     queries.append(map(int, raw_input().rstrip().split()))
    #
    # result = arrayManipulation(n, queries)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
