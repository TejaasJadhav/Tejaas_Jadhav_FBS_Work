#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)


#use random.randint(1000,9999)  using range function to generate 4 digit random number

uname= input('Enter UserID: ')
password = input('Enter Password: ')

userid= "Tejaas"
pass1= "Tejas123"
import random
if(uname==userid and password==pass1):
    captcha=random.randint(1000,9999)
    print(captcha)
    user_input = int(input("Enter the Captcha: "))
    if(captcha==user_input):
        print("Login Successfull!")
    else:
        print("Wrong Captcha!")
else:
    print("Login failed! Enter correct UserID and Password")
