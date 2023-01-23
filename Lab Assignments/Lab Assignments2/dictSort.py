dict1={5:4, 1:6, 6:3}
x=dict1.keys()

for i in range(len(dict1)):
    for j in  range(len(dict1)-1):
        if dict1[x[i]] > dict1[x[i+1]]:
            temp = dict1[x[i]]
            dict1[x[i]] = dict1[x[i+1]]
            dict1[x[i+1]] = temp

print(dict1)

print(x)