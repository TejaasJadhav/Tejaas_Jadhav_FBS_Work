
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


list=[1,8,2,3,5,7,10]

list.sort()
print(list)
ssmall=list[1]

print(len(list))  #length is total 7 so -2 after doing sort we get number

slarge=list[-2]

for i in list:
    if(i<ssmall):
        print(f"Second Smallest Number {ssmall}")

    if(i>slarge):
        print(f"Second Largest Number {slarge}")
