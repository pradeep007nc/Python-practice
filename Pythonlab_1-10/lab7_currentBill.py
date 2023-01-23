bill=int(input("Enter the units consumed"))
fixedAmt=50
totalbill=fixedAmt+0
if bill == 0:
    print("you have consumed 0 units bill is {}".format(fixedAmt))
elif bill > 0 and bill <= 100:
    print("units consumed is {} bill is {}".format(bill,totalbill+(bill*2.50)))
elif bill > 100 and bill <= 200:
    print("units consumed is {} bill is {}".format(bill,totalbill+(bill*3.10)))
else:
    print("units consumed is {} bill is {}".format(bill,totalbill+(bill*4.00)))