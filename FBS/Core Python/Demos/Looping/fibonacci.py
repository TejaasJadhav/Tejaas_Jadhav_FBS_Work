
n = int(input("How Many Fibonacci Numbers You Want :"))
a= -1
b= 1
for i in range(n):
    c = a+b
    print(c)
    a = b
    b = c