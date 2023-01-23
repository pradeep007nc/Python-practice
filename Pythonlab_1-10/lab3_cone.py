import math

diameter=int(input("enter the diameter of the cone"))
height=int(input("enter the height of the cone"))
radius=diameter/2

volume=math.pi*(math.pow(radius,2))*(height/3)

print("the volume is {:0.2f}".format(volume))