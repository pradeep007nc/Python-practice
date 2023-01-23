name=input("enter the name")

for i in range(0,len(name)):
    for j in range(0,i+1):
        print(name[j],end="")
    print()