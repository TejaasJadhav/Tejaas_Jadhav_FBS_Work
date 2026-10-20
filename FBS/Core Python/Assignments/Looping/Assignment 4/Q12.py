#12. Write a program to check if given number is Armstrong number or not.
# WAP to check if given number is Armstrong number or not
num = int(input("Enter a number : "))

# Step 1: count digits
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10

# Step 2: sum of digits raised to power count
temp = num
total = 0
while temp > 0:
    digit = temp % 10

    power = 1
    for i in range(count):      # digit * digit * ... (count times)
        power *= digit

    total += power
    temp //= 10

# Step 3: compare
if num > 0 and total == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is Not an Armstrong Number")