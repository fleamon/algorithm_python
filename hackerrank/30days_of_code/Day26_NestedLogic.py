#-*- encoding: utf-8


return_d, return_m, return_y = [int(x) for x in raw_input().split(' ')]
expected_d, expected_m, expected_y = [int(x) for x in raw_input().split(' ')]

if (return_y, return_m, return_d) <= (expected_y, expected_m, expected_d):
    print(0)
elif (return_y, return_m) == (expected_y, expected_m):
    print(15 * (return_d - expected_d))
elif return_y == expected_y:
    print(500 * (return_m - expected_m))
else:
    print(10000)


"""
9 6 2015
6 6 2015


45
"""
