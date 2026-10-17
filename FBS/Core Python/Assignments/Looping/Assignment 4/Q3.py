#WAP to print sum of series upto n.

n=int(input("Enter Number : "))
sum =0
for i in range(1,n+1):
    sum+=i
print(f"sum of series is {sum}")