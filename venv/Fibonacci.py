def fibo(n):
    a=0
    b=1
    if n<0:
        print("Invalid Input")
    elif n==1:
        print (a)
    else:
        print (a)
        print (b)
        for i in range (2,n):
            c = a + b
            a = b
            b = c
            if c>100:
                break
            else:
                print (c)

n= int(input("Enter the value for n"))
fibo(n)