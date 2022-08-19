def result(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd



lst= []
n=int(input("Enter the number of elements"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)
print(lst)

even, odd = result(lst)
print("No of even element", even)
print("No of odd element", odd)