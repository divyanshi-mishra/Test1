def record (name, **data):
    print (name)
    print(data)
    for i,j in data.items():
        print(i,j)




record('Divyanshi', city='Mumbai', Age = 25, Mobile=992255)