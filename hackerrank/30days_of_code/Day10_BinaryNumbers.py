# -*- encoding: utf-8


def conBinCnt(n):
    arr = []
    binNum = str(bin(n).split('b')[1])
    arrOne = binNum.split('0')
    for i in range(0, len(arrOne)):
        arr.append(len(arrOne[i]))
    return max(arr)


if __name__ == '__main__':
    # n = int(input())
    n = 345667445
    print conBinCnt(n)

