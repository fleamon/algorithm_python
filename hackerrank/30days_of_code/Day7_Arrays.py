# -*- encoding: utf-8


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())

    print " ".join(str(i) for i in arr[::-1])
