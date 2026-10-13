#Write a Program to input two angles from user and find third angle of the triangle.

angle1 = int(input("Enter First angle of Triangle:"))
angle2 = int(input("Enter Second Angle of Triangle:"))
angle3 = 180 -(angle1 + angle2)
print(f"Missing Angle of Triangle is:{angle3}° degrees")