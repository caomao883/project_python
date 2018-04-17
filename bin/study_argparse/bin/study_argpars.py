import argparse
script_name = "ouhuihao"
parser = argparse.ArgumentParser(description = script_name + "run script", formatter_class = argparse.RawTextHelpFormatter)
parser.add_argument('-d','--date',default="20180305")
arg = parser.parse_args()
print(arg.date)