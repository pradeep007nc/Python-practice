
n=5
var=1
for i in range(0,n):
    for j in range(0,i+1):
        print(f"{var} ",end="")
        var+=1
    print()