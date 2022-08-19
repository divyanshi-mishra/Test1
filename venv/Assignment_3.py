def B(i,lst):
    for j in lst:
        if (i is j):
            print("They have same identity")

lst= []
n=int(input("Enter the number of elements"))
for i in range (0,n):
    ele=(input())
    lst.append(ele)
print(lst)

for i in lst:
    if i == 'Switch':
        B(i,lst)
        break
else:
    print("They have different identity")




# if 'x' in list:
#    print("")