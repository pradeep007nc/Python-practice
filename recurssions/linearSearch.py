list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def linearSearch(list1, start, length, ele):
    if list1[start] == ele:
        return start
    if start == length:
        return -1
    return linearSearch(list1, start+1, length, ele)

print(linearSearch(list1, 0, len(list1)-1, 30))