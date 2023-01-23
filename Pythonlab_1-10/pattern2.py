size=7
for i in range(size,0,-1):

    for j in range(0,2*size-1):
        print(" ",end="")

    for k in range(1,size-i):
        print(f"{k}",end="")

    print()