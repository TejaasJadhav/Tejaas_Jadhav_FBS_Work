#Find the sum of three-digit number.

d= int(input("Enter Three Digit Number :"))

hundred_digit =  d/100
tens_digit = (d/10)%10
units_digit = d%10     #reminder use % (modulus)
sum = int(hundred_digit+tens_digit+units_digit)

print(f"Sum of Three-digit Number is : {sum}")