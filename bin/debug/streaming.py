#!/usr/bin/env python                                                                                                                                                                                                                   
# -*- coding: utf-8 -*-

"""
File: streaming.py
Author: ouhuihao(ouhuihao@oppo.com)
Date: 2018/3/24 16:15
"""
import sys


def counter(inf, count=1):
    print >> sys.stderr, "reporter:counter:group,%s,%d" % (inf, count)


for line in sys.stdin:
    data = line.strip("\n\r").split("\t")
    try:
        a = ""
        b = int(a)
    except:
        print("dfasf")
        s = sys.exc_info()
        #本地调试
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        #集群调试
        #counter("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))