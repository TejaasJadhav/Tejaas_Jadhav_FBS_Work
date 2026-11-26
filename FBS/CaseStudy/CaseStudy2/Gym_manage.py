from gm import member
from Trainer import trainer

class gym_manage:
    Gymdetails={}
    def addmember(self):
        gym=None
        mid=int(input("Enter GYM ID :"))
        if mid in gym_manage.Gymdetails:
            print("Member Already Exist")
        else:
            mname=input("Enter Name of Memebr :")
            mshi=int(input("Enter Membership Plan Type \n(1) for 3Months\n (2) for 6Months\n (3) for 1Year\n Pick Plan :"))
            if mshi in (1, 2, 3):
                fees = int(input("Enter Fees :"))
                gym= member(mid, mname, mshi, fees)
                print(f"Member Added to Gym -------> {mname}")
            else:
                print("Invalid Input>>>>!")
        gym_manage.Gymdetails[mid]=gym
        print(f"{mname} You Are Welcomed to GYM")

    def removem(self):
        mid=int(input("Enter Memebr ID :"))
        if mid in gym_manage.Gymdetails:
            del gym_manage.Gymdetails[mid]
            print(f"Member with {mid} Id Deleted..")
        else:
            print(f"{mid} Member does not Exists")

    def displaym(self):
            if not gym_manage.Gymdetails:
                print("Employee Not Exists")
            else:
                for values in gym_manage.Gymdetails.values():
                  print(f"{values}")

    def appointtrainer(self):
        mid=int(input("Enter Member ID :"))
        if mid not in gym_manage.Gymdetails:
            print(f"{mid} Member Not Exits")
            return
        tid=int(input("Enter Trainer ID :"))
        tname=input("Enter Trainer Name :")
        salary=float(input("Enter Salary :"))
        t=trainer(tid,tname,salary)
        gym_manage.Gymdetails[mid].trainer=t
        print(f"{tname} is Appointed as Trainer for {gym_manage.Gymdetails[mid].name}")

    def Renewm(self):
        mid=int(input("Enter Member ID :"))
        if mid in gym_manage.Gymdetails:
            plan=input("Pick Renew Plan (3Months/6Months/1Year)")
            gym_manage.Gymdetails[mid].mshi=plan
            print(f"{gym_manage.Gymdetails[mid].name} Membership Updated for {plan}")
        else:
            print("Member Not Exits")
