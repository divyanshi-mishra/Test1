import array as arr
vals = arr.array('i', [23,12,56,78,90])
print("Original array is: ")
for i in vals:
    print(i)

print ()

print("Reverse Array is: ")
vals.reverse()
e=0
while e<len(vals):
    print (vals[e])
    e+=1