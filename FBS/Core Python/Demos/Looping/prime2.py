#WAP a program to print prime numbers form 1 to n 

n = int(input("Enter number : "))
if(n>1):
    for j in range(2,n+1):
        for i in range(2,j):
            if(j%i==0):
                break
        else:
            print(j)
else:
    print("The Number is less than 2")