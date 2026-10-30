li=[5,2,1,7,3]
print("Before Sorting",li)
for i in range(len(li)-1):     #Start 0 By default
    si=i
    for j in range(i+1,len(li)):
        if li [si]>li[j]:
            si=j
        li[i],li[si]=li[si],li[i]
print("After Sorting",li)