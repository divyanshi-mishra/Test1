
def code(b):
    print(type(b))
    for j in b:
        if j == "apple":

            a=j
            return a
            break
    else:
        print("Fruit Apple is not available")


lst= []
n=int(input("Enter the number of elements"))
for i in range (0,n):
    ele=(input())
    lst.append(ele)
print(lst)

result=code(lst)

print("Printing the variable on which apple is stored : ", result)