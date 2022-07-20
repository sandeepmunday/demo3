n = int(input("enter any number: "))
if n>1:
    for j in range (2,n):
        if (n %j) == 0:
            print(n,"it is not prime number")
            break
        else:
            print(n,"it is prime number")
            break
else:
    print(n,"it is not prime number")
