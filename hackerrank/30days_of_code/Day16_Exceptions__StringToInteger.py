#!/usr/bin/env python
# -*- encoding: utf-8

import sys

S = raw_input().strip()

try:
    print int(S)
except:
    print "Bad String"
