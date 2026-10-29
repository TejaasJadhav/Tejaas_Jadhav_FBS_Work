def SearchElement(li,tar):
    #for var in li:
    #if tar==var:
    # return True
    #else:
    #return false
    for i in range(len(li)):
        if li[i]==tar:
            return i
        else:
            return-1
        #es=SearchElement(li,tar)
        #if res:
        #if searchElement(li,tar):
        #print("Element Found")
        #else:
        # print("Element not Found")
    li=[12,56,7,88,18]
    tar=int(input("Enter Element to search..."))
    res=SearchElement(li,tar)
    if res==-1:
        print("Element Is not Found")
    else:
        print(f"Element is found at index {res}")