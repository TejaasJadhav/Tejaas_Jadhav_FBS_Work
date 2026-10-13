#Write a program to input angles of a triangle and check whether triangle is valid or not. 

a1= int(input("Enter First Angle: "))
a2 =int(input("Enter Second Angle: "))
a3 = int(input("Enter Third Angle: "))

triangle = a1+a2+a3

if(triangle ==180):
    print(f"Measure of angles is {triangle} and it is Valid Triangle")
else:
    print(f"Measure of angles is {triangle} Degree and it is Invalid Triangle")