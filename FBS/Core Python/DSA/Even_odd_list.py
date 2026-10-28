#sum of Even and odd number form list

list=[1,2,5,9,10,11,17,3]
even=0
odd=even

for i in list:
    if(i%2==0):
        even+=i
    if(i%2!=0):
        odd+=i
print(f"Sum of Even Numbers : {even}")
print(f"Sum of Odd Numbers : {odd}")