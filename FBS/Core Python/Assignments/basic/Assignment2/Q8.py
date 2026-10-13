#Write a program to swap two numbers using third variable.

num1=int(input("Enter Number 1 :"))       #num1=10
num2=int(input("Enter Number 2 :"))       #num2=20
print(f"before Swap: {num1}&{num2}")     #10&20
box = num2         # box hold memory address of num2    : box =20
num2= num1         # num2 hold num1 address             : num2 =10
num1 = box         # num1 holds box address values swap : num1 = 20

print(f"After Swap: {num1}&{num2}")   #20&10 