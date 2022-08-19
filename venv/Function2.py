def update(x):
    x=8
    print(id(x))
    print("x", x)

a=9
print(id(a))
update(a)
print(id(a))
print("a", a)