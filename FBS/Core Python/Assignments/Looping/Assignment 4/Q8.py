#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
n= int(input("Enter Number : "))
for i in range(1,n+1):
    if(i%7==0 or i%5==0):
        print(i,end=" ")
print()
print(f"Numbers divisible by 7 and multiple of 5 in range 1 to {n}")
