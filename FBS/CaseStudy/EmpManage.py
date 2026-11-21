from HR import Hr
from Dev import Dev
from Emp import Employee

class Empmanage:
    empDetails={}
    def addemp(self):
        emp=None
        id=int(input("Enter Emp Id :"))
        if id in Empmanage.empDetails:
            print("employee already Exist")
        else:
           ename=input("Enter Emp Name :")
           esal=int(input("Enter Salary :"))
           etype=int(input("Enter Emp Type(1 for HR / 2 for Dev):"))
        if etype==1:
            com=int(input("Enter HR Commission :"))
            emp=Hr(id,ename,esal,com)
        elif etype==2:
            ebonus=int(input("Enter Developer Bonus: "))
            emp=Dev(id,ename,esal,ebonus)
        else:
               print("Invalid Input....")
        Empmanage.empDetails[id]=emp  
        print("Employee Created Successfully...!")

            
    def displayemp(self):
        if not Empmanage.empDetails:
            print("Employee Not Exists")
        else:
            for values in Empmanage.empDetails.values():
              print(f"{values}")
    def searchemp(self):
        eid=int(input("Enter Emp ID :"))
        if eid in Empmanage.empDetails:
            print(Empmanage.empDetails[eid])
        else:
            print("employee with this id is not found")
    def updateemp(self):
        eid=int(input("Enter Emp ID :"))
        if eid in Empmanage.empDetails:
            newName=input("Enter New Name :")
            Empmanage.empDetails[eid].setName(newName)
            print("Name is Updated Successfully")
    def deleteemp(self):
        eid=int(input("Enter Emp ID :"))
        if eid in Empmanage.empDetails:
            print(f"Employee with {eid} Id is Deleted Successfully...")
        else:
            print("Employee Does not Exists :")
            return