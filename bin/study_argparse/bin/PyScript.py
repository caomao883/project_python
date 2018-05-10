import argparse
class PyScript(object):
    def __init__(self):
        script_name = "ouhuihao"
        self.parser = argparse.ArgumentParser(description=script_name + "run script", formatter_class=argparse.RawTextHelpFormatter)
        self.parser.add_argument('-d', '--date', help="input a date argument")
        self.parser.add_argument('-t', '--task_type', default='hadoop')
        self.arg = self.parser.parse_args()
