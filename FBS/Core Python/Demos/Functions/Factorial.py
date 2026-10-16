def fact(num):
    mult = 1
    for i in range(2,num+1):
        mult*=i
    return mult
n = int(input("Enter Number for Fatorial: "))
result= fact(n)
print("Factorials:",result)