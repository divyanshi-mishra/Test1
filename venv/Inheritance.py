class A:

    def __init__(self):
        print("In A init")

    def func1(self):
        print("I am func1")

    def func2(self):
        print("I am func2")

class B:


    def func3(self):
        print("I am func3")

class C(A,B):    #Multiple Inheritance

    def __init__(self):
        super().__init__()     #because it goes left to right(Method Resolution Order)
        print("In C init")

    def func4(self):
        print("I am func4")
        super().func1()

class D(A): #Single Inheritance

    def __init__(self):
        super().__init__()
        print("In D init")


c1=C()
d1=D()

c1.func3()
c1.func2()
c1.func4()


