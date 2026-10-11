#WAP to do sum of digit 


num = int(input("Enter Number: "))
sum =0                     #variable initialization
while(num>0):              #condition used
    d = num%10
    sum+=d                # value should change
    num = num//10      #used to execute sum of last stage
        
print(f"Sum of Digit :{sum}")


#### while Loop :
#                 Used when you wanna to execute condition multiple times And case when            
#                 you dont know how much times loop has to execute (unpredicated)