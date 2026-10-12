#Program to Find the Roots of a Quadratic Equation

a = float(input("Enter Value of a:"))
b = float(input("Enter Value of b:"))
c = float(input("Enter Value of c:"))

delta= (b**2) - (4*a*c)
if delta > 0:
    root1 = (-b+delta**0.5)/(2*a)
    root2 = (-b-delta**0.5)/(2*a)
    print(f"Roots of Quadratic Equation are: {root1} & {root2}")
elif delta ==0:
    x = -b/(2*a)
    print(f"There is One Root:{x}")
else:
    print("roots are imaginary not Available, Delta < 0")