#WAP to print all numbers in a range divisible by a given number.
#range 1 to 100
n= int(input("Enter Number : "))
for i in range(1,101):
    if(i%n==0):
        print(i,end=" ")
        
print(f"are Numbers in range divisible by {n}")