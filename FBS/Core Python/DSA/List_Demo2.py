
#largest and smallest from list
lis=[1,2,4]
largest=lis[0]
small=lis[0]
for i in range(1,len(lis)):
    if lis[i]>largest:
        largest=lis[i]
    if lis[i]<small:
        small=lis[i]
print(f"Largest Number form list = {largest}")            
print(f"Smallest Number form list = {small}")

#2 largest number and 2 smallest number