import random
import copy

def checkEqual(santa, secret_santa):             #it checks for all indexes wehther both elements at same index are not same
    for i in range(len(santa)):
        if santa[i] == secret_santa[i]:
            return False
    return True


santa = ['vaibhaw', 'vinayak', 'pradeep', 'vishnu']   #list1
secret_santa = copy.deepcopy(santa)                   #creating list2 using deecopy in order to avoid python pointing to same list

while True:
    if checkEqual(santa, secret_santa):
        for i,(sender,reciever) in enumerate(zip(santa, secret_santa)):   #zip it and run in single loop
            if sender != reciever:                                        #print values of both list inividually
                print(f"{sender}:{reciever}")
        break                                      #break loop if sucessful
    else:
        random.shuffle(secret_santa)                                 #shullfe till checkequal becomes true







