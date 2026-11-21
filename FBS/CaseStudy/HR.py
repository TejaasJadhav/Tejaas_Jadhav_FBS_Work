
from Emp import Employee

class Hr(Employee):
    def __init__(self, id, name, sal,com):
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