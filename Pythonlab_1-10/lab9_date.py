
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

date=int(input("enter date"))
mon=int(input("enter month"))
year=int(input("enter year"))

print(f"the date is {date}-{month[mon-1].upper()}-{year}")