#!/usr/bin/env python
# -*- encoding: utf-8

import re

if __name__ == '__main__':
    N = int(raw_input())
    ans = []

    for N_itr in xrange(N):
        firstNameEmailID = raw_input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.search('@gmail\.com$',emailID):
            ans.append(firstName)
    ans.sort()
    for i in ans:
        print i

"""
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com


julia
julia
riya
samantha
tanya
"""
