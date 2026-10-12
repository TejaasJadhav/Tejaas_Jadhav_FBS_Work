#WAP to check if person is eligible to marriage or not

gender = input("Enter Gender (Male/Female): ")
age = int(input("Enter Age: "))

if(gender== "Male"):
    if(age>=21):
        print("You are eligible for marriage")
    else:
        print("You are not eligible for marriage")
else:
    if(age>=18):
        print("You are eligible for marriage")
    else:
        print("You are not eligible for marriage")  
