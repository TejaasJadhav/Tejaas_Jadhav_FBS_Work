
from Emp import Employee


class Dev(Employee):
    def __init__(self, id, name, sal,bonus):
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