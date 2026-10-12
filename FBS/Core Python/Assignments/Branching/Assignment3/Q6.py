#Write a program to calculate profit or loss.

cost_price= float(input("Enter Cost Price : "))
sell_price = float(input("Enter Selling Price : "))

if(sell_price>cost_price):
    print("profit")
elif(sell_price<cost_price):
    print("loss")
else:
    print("Break Even")