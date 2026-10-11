#1 pass: to neglect expected indentation error


#for i in range(1,10):
#    pass



#2 Break: Terminate the loop 
 # for i in range(1,6):
#      if(i==3):
#        break            (break stops the loop)
#      print(i)



#3  Continue : Stop the current Iteration
#    for i in range(1,6):
#        if(i==3):
#           continue
#        print(i)


#4   else : will execute when (for loop) is executed successfully.

for i in range(1,6):
    if(i ==3):
        continue       # here continue stop iteration of 3 . loop is not stoped it will execute successfully
    print(i)           # if we used break then loop stoped and else will not execute because for loop is not executed successfully
else:
    print("Else Executed:")