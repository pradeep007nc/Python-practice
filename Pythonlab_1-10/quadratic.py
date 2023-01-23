import math

a=int(input("enter first coefficient:"))
b=int(input("enter Second coefficient:"))
c=int(input("enter Third coefficient:"))

determinant=b*b-4*a*c


if determinant>0:
    print("Roots are real")
    root1=-b+(math.sqrt(determinant)/(2*a))
    root2=-b-(math.sqrt(determinant)/(2*a))
    print("roots are {} {}".format(root1,root2))

elif determinant==0:
    print("Single root")
    print(-b/(2*a));

else:
    print("roots are imaginary")
    sqrt_val=math.fabs(determinant)
    print(- b / (2 * a), " + i", sqrt_val)
    print(- b / (2 * a), " - i", sqrt_val)