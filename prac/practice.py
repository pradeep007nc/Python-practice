list1=[0,1,0,0,1,0,0,1,0,0,1]
size=len(list1)
list2=[0]*size
left=0
right=size-1

for i in range(0,size):
    if list1[i]==0:
        list2[left]=list1[i]
        left+=1
    else:
        list2[right]=list1[i]
        right-=1

print(list2)