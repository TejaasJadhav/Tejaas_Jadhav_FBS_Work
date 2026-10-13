#Program to find quotient and remainder of two numbers.

divident = int(input("Enter Dividend:"))
divisor = int(input("Enter Divisor:"))
quotient = (divident//divisor)
remainder= divident%divisor
print(f"Quotient of Given Numbers is: {quotient} & Remainder of Given Numbers is: {remainder}")