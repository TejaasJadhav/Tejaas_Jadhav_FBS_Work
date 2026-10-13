#Write a program to reverse three-digit number.

num1 = int(input("Enter 3 Digit Number : "))

hundred = int(num1%10)
ten = int((num1/10)%10)
unit = int(num1/100)

total= (hundred*100)+(ten*10)+(unit*1)

print(f"After reverse : {total}")