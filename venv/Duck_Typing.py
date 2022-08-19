class Laptop:
    def execute1(self):
        print("I am lovely")
        print("I am pretty")

class MyEditor:

    def execute(self):
        print("I am lovely")
        print("I am pretty")
        print("I am fantabulous")

class Result:

    def code(self, ide):
        print("Yes")
        ide.execute()

class Result1:

    def code1(self, ide1):
        print("NO")
        ide1.execute1()


ide=MyEditor()
ide1=Laptop()
r1=Result()
r2=Result1()
r1.code(ide)
r2.code1(ide1)