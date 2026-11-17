class Mec:
    def display(self):
        print("I am from Dispaly of MEc ")
class Electrical:
    def display(self):
        print("I am from Display of  Electrical ")
class Mectronix(Mec,Electrical):
    pass
    # def display(self):
    #     print("I am from Mectronix ")

m=Mectronix()
m.display()