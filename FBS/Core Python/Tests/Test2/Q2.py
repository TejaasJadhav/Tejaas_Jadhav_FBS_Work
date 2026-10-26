

n = int(input("Enter a 3 digit number: "))

a = n // 100          # 2
b = (n // 10) % 10    # 1
c = n % 10            # 4

if a == 2 * b and c == 2 * a:
    print("Yes, you have done it")
else:
    print("Please try next time")