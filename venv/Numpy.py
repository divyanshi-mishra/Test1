from numpy import *

arr=array([2,4,54,6,7], int)
print(arr.dtype)
print(arr)

arr1=linspace(0,16,10)
print(arr1)
arr2=arange(1,15,2)
print(arr2)
arr3=linspace(0,16,10)
print(arr3)
arr4=zeros(5, int)
print(arr4)
arr5=ones(5, int)
print(arr5)

arr6= arr+8
print(arr6)

arr7=arr+arr6
print(arr7)

print(sin(arr))
print(log(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))
print(concatenate ((arr,arr6) ))

arr6=arr
print(arr6)

print(id(arr))
print(id(arr6))

arr6=arr.view()
print(id(arr))
print(id(arr6))

arr[1]=7
print(arr6)
print(arr)

arr6=arr.copy()
arr[1]=8
print(arr6)
print(arr)