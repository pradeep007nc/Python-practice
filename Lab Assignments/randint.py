import random

def remove_repeated(list1):
    list2=set(list1)
    list1=list(list2)
    print(list1)

list1=[]
for i in range(50):
    list1.append(random.randint(50,100))

print(f"{list1}")
remove_repeated(list1)
