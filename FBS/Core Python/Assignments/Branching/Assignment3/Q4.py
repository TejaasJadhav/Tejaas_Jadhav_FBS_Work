#Write a program to input all sides of a triangle and check whether triangle is valid or not. 

a= float(input("Enter first Side : ") )
b = float(input("Enter Second Side : "))
c = float(input("Enter Third Side : "))

if(a+b>c and a+c>b and b+c>a):
    print("The Triangle is Valid")
else:
    print("The Triangle is Invalid")