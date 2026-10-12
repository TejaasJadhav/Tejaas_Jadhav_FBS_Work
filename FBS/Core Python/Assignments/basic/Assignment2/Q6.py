#WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

salary = float(input("Enter salary of Employee :"))
da = 0.10*salary
ta = 0.12*salary
hra =0.15*salary

total_salary = salary+da+ta+hra
print(f"Total Salary of Employee Based on Basic is : {total_salary} Rs")