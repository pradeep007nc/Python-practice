import copy

str1=[]
asc=97
str2=[0]*26
left=0
right=len(str1)-1

for i in range(26):
    str1+=chr(asc)
    asc+=1

def swap():
    for i in range(26):
        temp = str1[right]
        if i == 0:
            str2[i] = temp
        str2[i] = str1[i-1]
    print(str2)



for i in range(26):
    swap()
    str1=str2.copy()



