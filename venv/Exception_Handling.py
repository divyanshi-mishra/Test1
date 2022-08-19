a=9
b=3

try:
    print("File Open")
    print(a/b)
    a=int(input("Enter the value for a : "))
    print(a)

except ValueError as v:
    print("Invalid input", v)

except ZeroDivisionError as e:
    print("You cannot divide a number by 0", e)

except Exception as e:
    print("Sone other exception", e)

finally:
    print("Close File")
    print ("Have a nice day")