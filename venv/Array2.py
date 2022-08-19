from array import *

arr=array("i", [])

n=int(input("ENter the length of array : "))
for i in range(n):
    value = int(input("Enter the next value : "))
    arr.append(value)

print(arr)

search =int(input("Enter the value for search : "))


for e in arr:
    if e==search:
        print(arr.index(search))
        break
else:
    print("not found in the array")


