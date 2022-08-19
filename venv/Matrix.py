from numpy import *

arr = array([
    [1,3,5,7],
    [2,4,6,8]
])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr2=arr.flatten()
print(arr2)
arr3=arr2.reshape(2,4)
print(arr3)
arr2=array([2,5,6,7,8,9,1,2,56,23,12,89])
arr4=arr2.reshape(2,2,3)
print(arr4)

