
server_os = {'windows':1,'unix':2,'linux':3}

def my_function(server_os):

    for i,j in server_os.items():

        if i == 'windows':

            print(j)

        elif i == 'unix':

            print("Yes!we found unix")

        else:

            print("Yes!we found all the vmware os !!")



my_function(server_os)

#replace method in python.