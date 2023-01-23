str1 = "malayalam"
length = len(str1)-1
start = 0
mid = length/2

def palind(str1, start, mid, end):
    if start == mid or end == mid:
        return True
    if str1[start] != str1[end]:
        return False
    return palind(str1, start+1, mid, end-1)

if palind(str1, start, mid, length):
    print("its palindrome")
else:
    print("its not palindrome")

