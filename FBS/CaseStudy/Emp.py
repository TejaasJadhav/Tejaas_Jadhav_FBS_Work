

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
        