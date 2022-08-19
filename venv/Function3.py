def sum(a, *b):            #variable length argument
    c=0
    for i in b:
        c=c+i

    result=c+a

    print(a)
    print(b)
    print(c)
    print(result)

sum(3,4,5)

def result(name, age=18):       #Default Argument
    print(age)
    print(name)

result('aman')

def result(name, age):       #Keyword Argument
    print(age)
    print(name)

result(age=19,name='aman')