#Write a program to check if given 3 digit number is a palindrome or not.


num1 = int(input("Enter 3 Digit Number : "))

hundred =int(num1%10)
ten = int((num1/10)%10)
unit = int(num1/100)

total= (hundred*100)+(ten*10)+(unit*1)

if(num1==total):
    print(f"{num1} is a Palindrome Number")
else:
    print(f"{num1} is Not a Palindrome Number ")