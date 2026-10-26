
r= float(input("Enter radius of half Circle field")) #20
rec_length = float(input("Enter length of rectangle Field"))#50
rec_breadth = float(input("Enter breadth of rectangle Field")) #40
half_circle_field = float((3.14*r*r)/2)

rec_field = rec_length*rec_breadth

total_area = float(half_circle_field+rec_field)
total_cost = (total_area*35)*5

print(f"Total Cost for 5 times Barbed wire Fencing is {total_cost} Rs")