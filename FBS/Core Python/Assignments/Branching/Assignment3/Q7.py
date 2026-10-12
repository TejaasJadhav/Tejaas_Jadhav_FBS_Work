#Write a program to check if user has entered correct userid and password.

uname = input("Enter User Name : ")
pwd = input('Enter Password :')

uid = "admin"
upwd ="admin123"

if(uname==uid and pwd==upwd):
    print("Correct credentials")
elif(uname!=uid and pwd!=upwd):
    print("Incorrect Username and Password")
else:
    if(uname!=uid and pwd==upwd):
        print("Incorrect Username")
    else:
        print("Incorrect Password")