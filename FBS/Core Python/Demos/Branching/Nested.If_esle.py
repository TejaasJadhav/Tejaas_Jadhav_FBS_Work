#WAP a program for Marriage Eligiablitiy

gender = input("Enter Gender(Male/Female): ")
age = int(input("Enter Age :"))

if(gender=='Male'):
    if(age>=21):
        print("You are Eligible for Marriage")
    else:
        print("paisa Kama le pehle")
else:
    if(age>=18):
        print("You are Eligible for Marriage")
    else:
        print("sapne Puree Karo ")