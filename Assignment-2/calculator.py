n1 =int(input("enter 1st number: "))
n2 =int(input("enter 2nd number: "))

print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for division")

n =int(input("enter operation: "))
if n==1:
    print(n1+n2)
elif n==2:
    print(n1-n2)
elif n==3:
    print(n1*n2)
elif n==4:
    print(n1/n2)
else:
    print("enter valid operation")
