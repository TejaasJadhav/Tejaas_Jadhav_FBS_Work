class Employee:
    def _init_(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname
    
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    
    def display(self):
        print(f"Id={self.id} NAme={self.name} Sal={self.sal}")
    
    def calSal(self):
        print("Final Sal of Employee=",self.sal)

class Hr(Employee):
    def _init_(self, id, name, sal,com):
        super()._init_(id, name, sal)
        self.com=com
    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom
    def display(self):
        super().display()
        print(f"Com= {self.com}")
    def calSal(self):
        print(F"Sal of HR= {self.com+self.sal}")
    
class Dev(Employee):
    def _init_(self, id, name, sal,bonus):
        super()._init_(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,nbonus):
        self.bonus=nbonus
    def display(self):
        super().display()
        print(f"Bonus= {self.bonus}")
    def calSal(self):
        print(f"Sal of Devloper = {self.sal+self.bonus}")
        
e=Employee(1,"Rahul",234556)
d=Dev(18,"Virat",747474,1000)
h=Hr(13,"Haraman",557474,100)
e.calSal()
d.calSal()
h.calSal()