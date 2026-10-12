#Calculate the cost of painting the following building’s walls (both interior and
#exterior). You need to accept area (one wall) and cost of both interior and
#exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)

#formula Total cost = (8 × area × interior rate) + (7 × area × exterior rate)
area = float(input("Enter Area of One Wall : "))
ir = int(input("Enter Total interior Cost : "))
er = int(input("Enter Total Exterior Cost : "))

interior_cost = 8*area*ir
exterior_cost = 7*area*er

total_cost = interior_cost+exterior_cost
print(f"Total Cost to paint Walls is {total_cost} Rs")