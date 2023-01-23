n=5
lp=['A','B','C','D','E']
for i in range(0,n):
    for j in range(0,i+1):
        print(f"{lp[i]} ",end="")
    print()