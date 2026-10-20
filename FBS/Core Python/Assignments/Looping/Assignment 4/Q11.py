# WAP to check if given number is a Strong Number
num = int(input("Check if Number is Strong Number : "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10          # last digit

    fact = 1
    for i in range(2, digit + 1):   # factorial of this digit
        fact *= i

    total += fact              # add digit's factorial
    temp //= 10                # remove last digit

if num > 0 and total == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is Not a Strong Number")