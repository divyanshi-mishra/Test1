from numpy import *

m= matrix('2,3,4;3,4,5;6,7,8')
m1= matrix('2,3,4;3,4,5;6,7,8')

print(m)
print(diagonal(m))
print(m.min())
print(m.max())
print(m+m1)
print(m*m1)