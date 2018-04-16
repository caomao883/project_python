import sys
import os
CUR_DIR = os.path.dirname(os.path.realpath(__file__))

WORK_DIR = os.path.join(CUR_DIR,"..")
UTILS_DIR = os.path.join(CUR_DIR,"../utils")
sys.path.insert(0,WORK_DIR)
sys.path.insert(0,UTILS_DIR)
import utils.MyClass


class1 = utils.MyClass.Class1()
class1.func()