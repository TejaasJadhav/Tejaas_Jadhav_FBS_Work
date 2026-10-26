
year = int(input("Check if it is Leap Year or not:"))

if(year%4==0 and year%100!=0):
    print(f"{year} is Leap Year")
elif(year%100==0 and year%400==0):
    print(f"{year} is Leap Year")
else:
    print(f"{year} is not Leap Year")
    