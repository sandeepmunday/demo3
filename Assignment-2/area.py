import math
print("1 for circle")
print("2 for square")
print("3 for rectangle")
print("4 for triangle")
x = int(input("enter shape number: "))
if x==1:
    r = int(input("enter radius of circle:"))
    y = 2*math.pi*r
    print(y)
elif x==2:
    s = int(input("enter any side of square: "))
    z = 4*s
    print(z)
elif x==3:
    l = int(input("enter length of rectangle: "))
    b = int(input("enter breadth of rectangle: "))
    p = 2*(l+b)
    print(p)
elif x==4:
    b = int(input("enter base of triangle: "))
    h = int(input("enter height of triangle: "))
    a = (b*h)/2
    print(a)
else:
    print("enter correct shape number")


