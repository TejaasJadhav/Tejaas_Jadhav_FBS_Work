#with parameters & wit:h returning Values

def addition(num1,num2):     #function translate & execute
    sum=num1+num2            #only T after function call execute
    return sum               #only T  after function call execute

num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

res= addition(num1,num2)

print('Addition:',res)