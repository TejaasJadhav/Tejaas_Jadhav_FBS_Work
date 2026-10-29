#Slicing = breaking list into parts


li=[1,2,3,4,5]
n=int(input("Enter Element"))
for i in li:
    if(n==i):
        print("Yes Present")
        break
else:
    print("Not Found")