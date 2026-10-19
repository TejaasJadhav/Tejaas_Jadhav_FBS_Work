#WAP to check if given number is Perfect Number.
n= int(input("Check number is Perfect number or not : "))
divisor =0
for i in range(1,n):
    if(n%i==0):
        divisor += i
if(divisor==n):
    print(f"{n} perfect number")
else:
    print(f"{n} not perfect Number")