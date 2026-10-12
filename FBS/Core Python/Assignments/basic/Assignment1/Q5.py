#Write a program to enter P, T, R and calculate Compound Interest.

p = int(input("Enter Principal Amount:"))
r = float(input("Enter Rate of Interest:"))
t = int(input("Enter Time in Years:"))
ci = (p*(1+r/100)**t)
print(f"Compound Interest is:{ci}%")

