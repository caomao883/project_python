#coding:utf-8
import os
import sys

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
path1 = os.path.join(CUR_DIR,"../../utils")
path2 = os.path.join(CUR_DIR,"../../conf")
path3 = os.path.join(CUR_DIR,"..")
sys.path.insert(1,path1)
sys.path.insert(2,path2)
sys.path.insert(3,path3)
import Common
print(Common.aa)
print(__file__)
print(os.path.realpath(__file__))
print(CUR_DIR)
