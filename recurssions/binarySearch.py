list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def binarySearch(list1, start, length, ele):
    middle = int((start+length)/2)
    if start > length:
        return -1
    if list1[middle] == ele:
        return middle
    if list1[middle] > ele:
        return binarySearch(list1, start, middle-1, ele)
    return binarySearch(list1, middle+1, length, ele)

start =0
length = len(list1)-1

print(binarySearch(list1, start, length, 20))