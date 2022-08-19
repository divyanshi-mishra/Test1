from functools import reduce

f= lambda a,b: a+b
result=f(5,6)
print(result)

f= lambda a: a*a
result1=f(5)
print(result1)

def is_even(n):
    return n%2==0

nums=[3,7,8,9,2,4]
evens = list(filter(lambda n : n%2==0 ,nums))
doubles = list(map(lambda evens: evens * 2, evens))
sum = reduce(lambda a,b : a+b ,doubles)
print(evens)
print(doubles)
print(sum)