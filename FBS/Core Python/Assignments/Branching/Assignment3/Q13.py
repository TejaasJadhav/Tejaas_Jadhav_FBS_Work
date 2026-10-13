#Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill  

units = int(input("Enter number of units consumed: "))

bill = 0

# First slab (rate 0.50)
if units > 50:
    bill = bill + 50 * 0.50
else:
    bill = bill + units * 0.50

# Second slab (rate 0.75)
if units > 150:
    bill = bill + 100 * 0.75
elif units > 50:
    bill = bill + (units - 50) * 0.75

# Third slab (rate 1.20)
if units > 250:
    bill = bill + 100 * 1.20
elif units > 150:
    bill = bill + (units - 150) * 1.20

# Fourth slab (rate 1.50)
if units > 250:
    bill = bill + (units - 250) * 1.50

surcharge = bill * 20 / 100
total = bill + surcharge

print("Total bill: Rs.", total)

