#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

e = int(input("Enter English marks: "))
m = int(input("Enter Maths marks: "))
h = int(input("Enter Hindi marks: "))
s = int(input("Enter Science marks: "))
marathi = int(input("Enter Marathi marks: "))
total_sum = e+m+h+s+marathi
tpm = int(input("Enter Total Possible Marks: "))
percentage = (total_sum/tpm*100)
print(percentage)

if(percentage>=75):
   print("First Class and Distinction")
elif(percentage>=60 and percentage<=74):
   print("First Class")
elif(percentage>=50 and percentage<=59):
    print("Second Class")
elif(percentage>=40 and percentage<=49):
    print("Third Class")
else:
    print("Fail")