a=10

def value():
    a=9
    x=globals()['a']
    print(id(x))
    print('in fuc', a)
    globals()['a']=15

value()
print('outside', a)
print (id(a))
