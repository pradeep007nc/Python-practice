size=5
n=size/2
for i in range(0, size):

    for j in range(0,size-i):
        print(" ",end="")

    for k in range(0,2*i-1):
        print(f"*",end="")

    print()


