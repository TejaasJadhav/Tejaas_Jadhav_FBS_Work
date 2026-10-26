#Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:


length = float(input("Enter Length of figure :"))
breadth = float(input("Enter Breadth of figure :"))
radius = float(input("Enter Radius of figure :"))

rectangle_area = float(length*2*radius)
semicircle_area = float(0.5*3.14*radius**2)     #Area = (L × 2r) + (½ × π × r²)
area = float(rectangle_area + semicircle_area)    #Area = Area of rectangle + Area of semicircle
                                            #Area = (L × 2r) + (½ × π × r²)
#Perimeter = 2L + 2r + πr
perimeter = float(2*length+2*radius+3.14*radius)

print(f"Area of Figure is {area} cm")
print(f"Preimeter of Figure is {perimeter} cm")