#Write a program to calculate the percentage of student based on marks of any 5 subjects.

Subject1 = int(input("Enter marks of Subject 1:"))
Subject2 = int(input("Enter marks of Subject 2:"))
Subject3 = int(input("Enter marks of Subject 3:"))
Subject4 = int(input("Enter marks of Subject 4:"))
Subject5 = int(input("Enter marks of Subject 5:"))
totalmarks = int(input("Enter total marks of Examination:"))
totalmarks_obtained = Subject1+Subject2+Subject3+Subject4+Subject5
percentage = float(totalmarks_obtained/totalmarks)*100
print(f"Percentage of student: {percentage}%")