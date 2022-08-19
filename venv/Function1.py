def greet():
    print("Hello WOrld")

def add(x,y):
    c=x+y
    print(c)

def add_sub(a,b):
    x=a+b
    y=a-b
    return x,y

greet()
add(7,3)
value1, value2 = add_sub(8,9)
print(value1, value2)