#WAP to check if a given number is prime number or not.

n = int(input("Enter Number : "))
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print(f"{n} is Not Prime Number")
            break
    else:
        print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime NUmber")
