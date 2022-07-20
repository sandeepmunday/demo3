s = str(input("enter numbers to create list: "))
x = [int(i) for i in str(s)]
y = len(x)
avg = sum(x)/y
print(avg,"is avgerage of list")
print(max(x),"is maximum of list")
print(min(x),"is minimum of list")


