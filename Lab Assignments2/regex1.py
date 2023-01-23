str1=""" modi varanasi 2014 wins 
modi varanasi 2019 wins 
rahul Amethi 2014 wins 
rahul Amethi 2019 loses
rahul waynad 2019 wins 
Smrithi Amethi 2014 loses 
Smrithi Amethi 2019 wins 
Shah Gandhinagar 2014 wins 
Shah Gandhinagar 2019 wins"""

list1 = str1.lstrip().split("\n")
print(list1)

leaders = {}
elections = []
wincount=0
losscount=0

for i in list1:
    elections.append((i.split(" ")[2]))
    temp = i.split(" ")
    leaders.update({temp[0]: ['wins', 'loses']})
    temp.clear()


print(leaders)
print(elections)