#variable length Argument

#1 to pass multiple parameter to funaction
#2 mention single asterisk(*) symbol before para name in function definition
#3 all passed values stored in tuple format
#4 use for loop  to iterate values form tuple

def add(*data):
    sum =0
    for val in data:
        sum+=val
        return sum

    #num1=int(input())
    #num2=int(input())
    #num3=int(input())
    #num4=int(input())
res = add(10,20,30,40)    # here we direct put values in function call
print("Addition:" , res)