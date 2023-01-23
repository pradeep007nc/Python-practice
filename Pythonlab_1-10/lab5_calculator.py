sum=0
while True:
    inp1 = int(input("enter the first number"))
    inp2 = int(input("enter the second number"))
    oper = input("enter the operator b/w +,-,*,/")
    if oper == '+':
        sum=inp1+inp2
    elif oper == '-':
        sum = inp1-inp2
    elif oper == '*':
        sum = inp1*inp2
    elif oper == '/':
        sum = inp1/inp2
    else:
        print("enter operator only b/w +,-,*,/")

    print(f"the sum is {sum:.2f}")
