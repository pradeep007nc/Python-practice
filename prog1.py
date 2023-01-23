import random

rows,cols=(4,4)

#creating 2d list by iterating so that new list is created and same is not shared
list1=[[0 for i in range(rows)]for j in range(cols)]
sum=0
for i in range(rows):
    for j in range(cols):
        list1[i][j]=random.randint(0,9)
        sum+=list1[i][j]
print(list1)
print(sum)


