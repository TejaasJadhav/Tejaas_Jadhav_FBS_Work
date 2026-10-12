#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter first Angle: "))
b = int(input("ENter Second Angle: "))
c= int(input("Enter Third Angle: "))

d=a+b+c

if(a==b==c):
    if(d==180):
        print("The Triangle is Equilateral")
elif(a==b or b==c or a==c):
    if(d==180):
        print("The Triangle is Isosceles")
else:
    if(d==180):
        print("The Triangle is Scalene")
    else:
        print("The Triangle is Invalid")