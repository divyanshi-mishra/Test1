class object:
    color='red'
    def __init__(self):
        self.name = 'Divyanshi'
        self.age=25
        self.lap = self.Laptop()

    def update(self):
        self.age=90

    def compare(self,c2):
        if c1.age==c2.age:
            print("Same")
        else:
            print("Different")

    def show(self):
        print(self.name, self.age, self.lap.show())

    @classmethod
    def get_color(cls):
        return cls.color

    @staticmethod
    def get_printed():
        print("Good Bye")

    class Laptop:

        def __init__(self):
            self.brand ='HP'
            self.cpu='i5'

        def show(self):
            print(self.brand, self.cpu)



c1=object()
c2=object()
c1.update()
c1.compare(c2)
c1.show()
print(object.get_color())
print(object.get_printed())
