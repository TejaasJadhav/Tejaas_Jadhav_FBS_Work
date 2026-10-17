#WAP to print factorial of a number .

n=int(input("Enter Number : "))
mult=1
for i in range(2,n+1):
    mult*=i
print(f"Factorial {mult}")