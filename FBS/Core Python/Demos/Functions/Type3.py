#without parameters with returning values

def addition():
    num1= int(input("Enter Number1 : "))
    num2= int(input("Enter Number2 : "))

    sum = num1 + num2

    return sum
res = addition()
print(res)