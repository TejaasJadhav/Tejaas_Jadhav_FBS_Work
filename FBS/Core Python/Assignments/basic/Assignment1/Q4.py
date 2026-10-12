#Write a program to enter P, T, R and calculate simple Interest.

principal = int(input("Enter Principal Amount:"))
rateOfInterest = float(input("Enter Rate of Interest:"))
time= int(input("Enter Time in Years:"))
simpleInterest = float(principal*rateOfInterest*time)/100
print(f"Simple Interest is:{simpleInterest}%")