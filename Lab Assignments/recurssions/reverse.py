str1 = "pradeep"

def reverse(str1, str2, len):
    if len == 0:
        str2+=str1[len]
        return str2
    str2+=str1[len]
    return reverse(str1, str2, len-1)


str2 = ""
length = len(str1)-1
print(reverse(str1, str2, length))