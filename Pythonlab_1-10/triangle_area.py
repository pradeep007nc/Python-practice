import math

a=int(input("enter a side:"))
b=int(input("enter b side:"))
c=int(input("enter c side:"))
semi_permeter=a+b+c/2
area=math.sqrt(semi_permeter*(semi_permeter-a)*(semi_permeter-b)*(semi_permeter-c))
print("area is {:.2f}".format(area))