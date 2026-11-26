class member:
    def __init__(self,mid,name,mship,fees):
        self.mid=mid
        self.fees=fees
        self.name=name
        self.mship=mship
        self.trainer=None
    def getid(self):
        return self.mid
    def setid(self,newid):
        self.mid = newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def getmship(self):
        return self.mship
    def setmship(self,Nmship):
        self.mship=Nmship
        
    def __str__(self):
        text = (f"MID={self.mid}\nNAME={self.name}\n"
                f"Mship={self.mship}\nFees={self.fees}")
        if self.trainer:
            text += f"\nTrainer={self.trainer.name}"
        return text

    def display(self):
        print(self)
    def membership(self):
        print(f"Membership of {self.name} = {self.mship} ")
    
    

