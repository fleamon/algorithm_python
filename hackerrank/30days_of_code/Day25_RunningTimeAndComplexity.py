# -*- encoding: utf-8

n = input()
for i in range(0, n):
    chk = input()
    if chk == 1:
        print "Not prime"
    elif chk == 2:
        print "Prime"
    else:
        for i in range(2, int(chk ** 0.5) + 2):
            if chk % i == 0:
                print "Not prime"
                break
        else:
            print "Prime"


"""
3
12
5
7

Not prime
Prime
Prime
"""
