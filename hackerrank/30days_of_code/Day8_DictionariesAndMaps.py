# -*- encoding: utf-8


n = int(input())
name_numbers = {}
idx = 0
for i in range(0, n):
    name_number = raw_input().split()
    name_numbers[name_number[0]] = name_number[1]
# print name_numbers

for i in range(n, n + n):
    name = raw_input()
    if name in name_numbers:
        print "%s=%s" % (name, name_numbers[name])
    else:
        print "Not found"

