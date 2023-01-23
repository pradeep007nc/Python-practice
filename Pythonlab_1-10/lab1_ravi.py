import math

p=int(input("enter A to B:"))
q=int(input("enter B to C:"))
m=int(input("enter C to D:"))
n=int(input("enter D to e:"))

base=math.pow(p+m,2)
height=math.pow(q+n,2)

slant=math.sqrt(base+height)

print("the distance is {}:".format(slant))