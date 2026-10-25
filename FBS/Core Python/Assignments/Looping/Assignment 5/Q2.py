#2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
n = int(input("Enter Number of Students :"))
Mm= int(input("Enter Max Marks Can be scored:"))
total_per=0
for student in range(1,n+1):
    eng=int(input("Student Marks in English :"))
    mat=int(input("Student Marks in Maths :"))
    Hindi=int(input("Student Marks in Hindi :"))
    Marathi=int(input("Student Marks in Marathi :"))
    Sci=int(input("Student Marks in Science :"))
    ObtainedMarks = eng + mat + Hindi + Marathi + Sci   
    percentage = float(ObtainedMarks/Mm)*100
    print(f"Percentage of Student {student} {percentage} %")
    total_per+=percentage

average_per = total_per/n
print(f"Average Percentage of all {n} Students {average_per}%")
