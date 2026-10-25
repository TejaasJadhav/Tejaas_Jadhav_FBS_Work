#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_id = "TejasJadhav"
correct_pwd = "Tejas123"

for attempt in range(1, 4):          # 3 attempts: 1, 2, 3
    userid = input("Enter Username: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_pwd:
        print("Login successful")
        break                         # stop asking once login works
    print(f"Incorrect credentials. Attempts left: {3 - attempt}")
else:
    print("Too many failed attempts. Program terminated.")