list2={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
str = input();
for i in range(len(str)):
    val = int(str[i])
    print(f"{list2[val]}")