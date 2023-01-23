mks1=int(input("enter sub 1 marks"))
mks2=int(input("enter sub 2 marks"))
mks3=int(input("enter sub 3 marks"))
mks4=int(input("enter sub 4 marks"))
mks5=int(input("enter sub 5 marks"))

total = mks1+mks2+mks3+mks4+mks5
avg = total/5
percentage = (total/500)*100
cgpa = percentage/9.5
print("the percentage is {:2.2f} and cgpa is {:2.2f}".format(percentage,cgpa))