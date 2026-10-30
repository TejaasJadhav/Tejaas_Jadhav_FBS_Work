#Bubble Sort

li=[5,2,4,3,11,1]
print("Before Swapping=",li)
for i in range(0,len(li)-1):
    for j in range(0,len(li)-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print("after Swapping=",li)