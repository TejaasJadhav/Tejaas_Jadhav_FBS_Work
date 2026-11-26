from Gym_manage import gym_manage

class Mmain:
    def showdata(self):
        while True:
            print("1. add Memebr")
            print("2. Remove Member")
            print("3. Display Member")
            print("4. Appoint Trainer")
            print("5. Renew Membership")
            print("6. Exit")
            gg=gym_manage()
            choose=int(input("Enter Your Choice :"))
            if choose==1:
                gg.addmember()
            elif choose==2:
                gg.removem()
            elif choose==3:
                gg.displaym()
            elif choose==4:
                gg.appointtrainer()
            elif choose==5:
                gg.Renewm()
            elif choose==6:
                print("Exercise Ghar pe Kar>>>")
                break
            else:
                print("Invaild Input>>>")
m=Mmain()
m.showdata()
    