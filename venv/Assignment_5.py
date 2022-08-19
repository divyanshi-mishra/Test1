cars1=['ll','audi','maruti']
cars2=['kk','audi','renault']
flag=0
for i in cars1:
    if i == 'audi':
        print("‘200! yes we found Audi in list1’")
        flag=1
        break
else:
    for j in cars2:
        if j=='audi':
            print("‘200! yes we found Audi in list2’")
            flag=1
            break

if(flag==0):
    print("’404! Audi is not found’")