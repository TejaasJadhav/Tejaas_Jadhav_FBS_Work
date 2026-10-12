#Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)


p = int(input("Enter Principal Amount :"))
r = int(input("Enter Rate :"))
t = int(input("Enter Time in Years :"))

si= p*r*t/100
print(f"Simple Interest is {si}")