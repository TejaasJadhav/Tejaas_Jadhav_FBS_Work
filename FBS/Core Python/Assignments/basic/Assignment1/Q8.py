#Write a program to convert days into years, weeks and days.

total_days= int(input("Enter Total Number of days:"))
year = (total_days//365)
if year<1:
    print("Not Enough Days to Complete a Year")
week = (total_days//7)
if week<7:
    print("Not Enough Days to Complete a Week ")
print(f"Total Days into Year is:{year} Year & Week is:{week} week")