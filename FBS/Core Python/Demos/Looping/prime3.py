#WAP to find first n prime numbers
num=int(input("Enter Number : "))
i=2
count=0
while(count<num):
    for j in range(2,int(i**0.5)+1):    #used int because in range float value is not accepted so only takes int value
        if(i%j==0):
            break
    else:
            count+=1
            print(i)
    i+=1