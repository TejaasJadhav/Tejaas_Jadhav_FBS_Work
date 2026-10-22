#WAP to Calculate Sum of series

def sos(n):
    if(n<1):
        return 0
    else:
        return n+sos(n-1)

n=int(input("Enter Number :"))
res=sos(n)
print(res)