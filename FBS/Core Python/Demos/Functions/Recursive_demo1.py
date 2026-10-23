#Recursive Function

#Function Calling itself Directly or Indirectly

def seq(n):
    if(n>0):
        print(n)
        seq(n-1)
n=7
seq(n)