#def strin(a,b):
#    c=a+b
#    return c
# a=str("Geli")
# b=str(" Diwali")
# es=strin(a,b)
# print(res)

    #wap to add intgers

#    def inte(a,b):
#        c= a+b
#        return c

#    a=int(input("Enter Number 1 : "))
#    b=int(input("Enter Number 2 : "))
#    res=inte(a,b)
#   print(res)


#  def listadd(list1,list2):
#       finallist=list1+list2
#        return finallist
#    a=[1,2,3,4]
#    b=[11,22,44,55]

#   res=listadd(a,b)
#   print(res)

#WAP Calculate Time

class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec 

    def __add__(self,other):
        tse=self.sec+other.sec
        cmin=tse//60
        tse=tse%60
        tmin=self.min+other.min+cmin
        chr=tmin//60
        tmin=tmin%60
        thr=self.hr+other.hr+chr
        return Time(thr,tmin,tse)
    
    #def __add__(self,other):
    #    thr=self.hr+other.hr
    #    tmin=self.min+other.min
    #    tsec=self.sec+other.sec
    #    t=Time(thr,tmin,tsec)
    #   return t
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
t1=Time(12,45,56)
t2=Time(4,55,36)
t3=t1+t2
print(t3)

