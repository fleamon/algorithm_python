#!/usr/bin/env python
# -*- encoding: utf-8



if __name__ == '__main__':
    N = int(raw_input())
    if N % 2 == 1:
        print "Weird"
    else:
        if N >= 2 and N <= 5:
            print "Not Weird"
        elif N >= 6 and N <= 20:
            print "Weird"
        elif N > 20:
            print "Not Weird"

