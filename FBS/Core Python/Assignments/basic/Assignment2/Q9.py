#Write a program to swap two numbers without using third variable.

a = int(input("Enter Number :"))
b = int(input("Enter Number :"))
print(f"before swap Without using third Variable: {a}&{b}")
a=a+b    # a = 5 , b = 10    , 5+10=15  a=15
b=a-b    # b = 15-10 = 5     , b=5 step 1 solved
a=a-b    # a = 15-5 = 10     , a= 10 values swap without using third variable.
print(f"After swap : {a}&{b}")
