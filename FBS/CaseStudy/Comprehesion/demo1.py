#Normal way 

#    li=[1,22,24,56,33,21]
#    newlist=[]
#    for i in li:
#        if i%2==0:
#            newlist.append("Even")
#        else:
#            newlist.append("Odd")
#    print(newlist)

#Data Transforming 

li=[1,22,24,56,33,21]
newlist=["Even" if i%2==0 else "odd" for i in li]
print(newlist)