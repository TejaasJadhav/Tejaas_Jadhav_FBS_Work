#WAP to calculate selling price of book based on cost price and discount.

item_price = float(input("Enter Book Price :"))
discount = int(input("Enter Discount on Book :"))

selling_price = item_price*(1-discount/100)

print(f"selling price of Book is : {selling_price} Rs")