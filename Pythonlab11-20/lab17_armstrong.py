num=int(input())
temp=num
Sum=0
while temp>0:
    digit=temp%10
    Sum+=digit**3
    temp//=10

if num == Sum:
    print("its an armstrong number")
else:
    print("its not an armstrong number")


