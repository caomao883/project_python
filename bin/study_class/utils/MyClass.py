from MyClass2 import Class2
class Class1:
    def __init__(self):
        self.a = 1
        self.b = 2
    def func(self):
        print(".....")
        def func1():
            print("func1")
        class2 = Class2()
        class2.func(func1)