#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

count = 0
cur_line = ""
def counter(inf, count=1):
    print >> sys.stderr, "reporter:counter:group,%s,%d" % ( "_" + inf, count)
for line in sys.stdin:  # map的时候map中的key会被排序
    print >> sys.stdout,line
