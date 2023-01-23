n=5
var='A'
for i in range(0,n):
    for j in range(0,i+1):
        print(f"{var} ",end="")
        var=chr(ord(var)+1)
    print()