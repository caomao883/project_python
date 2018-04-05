#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

CUR_DIR = os.getcwd()
sys.path.insert(0, CUR_DIR)
import Commonconf

def counter(info, count=1):
    print >> sys.stderr, "reporter:counter:group,%s,%d" % (info, count)



for line in sys.stdin:
    if len(line) > 0:
        print >> sys.stdout,line
counter(CUR_DIR)
counter("......." + Commonconf.A)

