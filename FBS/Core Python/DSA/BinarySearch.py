def binarySearch(li):
    start = 0
    end = len(li) - 1
    tar = int(input("Enter The Element you want to search. "))
    while start <= end:
        mid = (start + end) // 2
        if tar == li[mid]:
            return mid
        elif tar > li[mid]:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1

li = [18, 25, 36, 47, 58, 69, 80]
res = binarySearch(li)
if res == -1:
    print("Element is not Found.")
else:
    print("Element is found at index", res)