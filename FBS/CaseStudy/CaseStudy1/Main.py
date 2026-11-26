from EmpManage import Empmanage
class main:
    def showmenu(self):
        while True:

            print("1. Add Employee")
            print("2. Display Employee")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
            em=Empmanage()
            choice = int(input("Enter Your choice :"))
            if choice==1:
                em.addemp()
            elif choice==2:
                em.displayemp()
            elif choice==3:
                em.searchemp()
            elif choice==4:
                em.updateemp()
            elif choice==5:
                em.deleteemp()
            elif choice==6:
                print("Thanks You....")
                break
            else:
                print('Invalid Choice')
m=main()
m.showmenu()