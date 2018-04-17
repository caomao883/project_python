import argparse
import PyScript
script_name = "ouhuihao"
parser = argparse.ArgumentParser(description=script_name + "run script", formatter_class=argparse.RawTextHelpFormatter)

def func1(parser):
    parser.add_argument('-d','--date',default="20180305")
    arg = parser.parse_args()
    print(arg.date)
#func1(parser)
def func2(parser):
    #python study_argpars.py -h
    parser.add_argument('-d', '--date',help="input a date argument")
    parser.add_argument('-t', '--task_type', default='hadoop')
    arg = parser.parse_args()
    print(arg.date)
    print(arg.task_type)


script = PyScript.PyScript()
print(script.arg.date)

