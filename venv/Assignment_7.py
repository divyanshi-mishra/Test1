def func(d):
    for key in d:
        if(d[key]=='Unix_Machine'):
            print("key:", key, "Value:", d[key], "Yes, we found unix'")
        elif(d[key]=='Windows_OS'):
            print("key:", key, "Value:", d[key], "Yes, we found Windows'")
        else:
            print("Yes, we found all the vmware os !!")

# Driver's code
D = {'a': 'Unix_Machine', 'b': 'Windows_OS', 'c':'lll', 'd':'ddff'}
func(D)

#items method in python - Optimized