zero=['zero','hundred']
one_digit=['one','two','three','four','five','six','seven','eight','nine']
ten_digits=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
last_digit=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

list1=[]
def num_length(x):
    num_count=0
    temp=x

    while temp != 0:
        temp1=temp%10
        temp=int(temp/10)
        list1.append(temp1)
        num_count+=1

    list1.reverse()
    return num_count

def num_to_word(user_input):
  try:

    number_length=num_length(user_input)

    if number_length>0 and number_length<=1:
        print(one_digit[list1[0]-1])

    elif number_length>0 and number_length<=2:
        if user_input>10 and user_input<20:
            print(ten_digits[list1[1]-1])
        elif list1[1]==0:
            print(last_digit[list1[0]-1])
        else:
            print(last_digit[list1[0]-1],one_digit[list1[1]-1])

    elif number_length>0 and number_length<=3:
        if list1[1]==0 and list1[2]==0 and list1[0]!=0:
            print(one_digit[list1[0]-1], zero[list1[1]-1])
        elif list1[2]==0:
            print(one_digit[list1[0]-1], zero[1], last_digit[list1[1]-1])
        elif list1[1]==1 and list1[2]==0 and list1[0]!=0:
            print(one_digit[list1[0]-1],zero[list1[1]], ten_digits[list1[1]-1])
        elif list1[1]==1 and list1[2]>0 and list1[2]<10:
            print(one_digit[list1[0]-1], zero[1], ten_digits[list1[2]-1])
        else:
            print(one_digit[list1[0]-1], zero[1], last_digit[list1[1]-1], one_digit[list1[2]-1])

  except:
    print("its not an integer please enter a integer")


user_input=int(input("enter a three digit number"))
num_to_word(user_input)







