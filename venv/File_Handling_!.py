f=open('hhrr.txt', 'r')
f1=open('hhrr_copy.txt', 'w')

for data in f:
    f1.write(data)