str1 = "hello sir have a good deed tum chutiya ho"
vowels = ['a', 'e', 'i', 'o', 'u']

def vow(str1, vowelCount, length):
    if length == 0:
        return vowelCount
    if str1[length] in vowels:
        vowelCount += 1
    return vow(str1, vowelCount, length-1)



length = len(str1)-1
vowelCount = 0
print(vow(str1, vowelCount, length))