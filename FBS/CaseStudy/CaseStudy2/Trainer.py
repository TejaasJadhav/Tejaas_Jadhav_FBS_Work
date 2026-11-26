from gm import member

class trainer(member):
    def __init__(self,tid,tname,salary):
        self.tid=tid
        self.tname=tname
        self.salary=salary
    def getsalary(self):
        return self.salary
    def setsalary(self,nsal):
        self.salary=nsal
    def __str__(self):
        return print(f"TID:{self.tid}\nNAME:{self.tname}\nSALARY:{self.salary}")
    def display(self):
        print(self)