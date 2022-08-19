class Computer:
    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram

    def printer(self):
        print("Result : ", self.cpu, self.ram)


div1= Computer('i5', 16)
div2=Computer('i7', 32)
div1.printer()
div2.printer()