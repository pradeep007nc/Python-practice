a=int(input("enter 1st large:"))
b=int(input("enter 2st large:"))
c=int(input("enter 3st large:"))

if a>b and a<c or a>c and a<b:
    print("a is 2nd largest")

elif b>a and b<c or b>c and b<a:
    print("b is 2nd largest")

else:
    print("c is 2nd largest")


