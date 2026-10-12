#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

p1= int(input("Enter Age of Person 1 : "))
ticket1 = int(input("Enter Ticket Amount : " ))
if (p1<12):
    fare1= ticket1*0.30
elif(p1>59):
    fare1= ticket1*0.50
else:
    fare1=ticket1
p2= int(input("Enter Age of Person 2 : "))
ticket2 = int(input("Enter Ticket Amount :" ))
if(p2<12):
    fare2=ticket2*0.30
elif(p2>59):
    fare2=ticket2*0.50
else:
    fare2=ticket2
p3= int(input("Enter Age of Person 3 : "))
ticket3= int(input("Enter Ticket Amount : " ))
if(p3<12):
    fare3=ticket3*0.30
elif(p3>59):
    fare3=ticket3*0.50
else:
    fare3=ticket3
p4= int(input("Enter Age of Person 4 : "))
ticket4= int(input("Enter Ticket Amount : " ))
if(p4<12):
    fare4=ticket4*0.30
elif(p4>59):
    fare4=ticket4*0.50
else:
    fare4=ticket4
p5= int(input("Enter Age of Person 5 : "))
ticket5= int(input("Enter Ticket Amount: " ))
if(p5<12):
    fare5=ticket5*0.30
elif(p5>59):
    fare5=ticket5*0.50
else:
    fare5=ticket5
total= fare1+fare2+fare3+fare4+fare5
print(f"Grand Total of 5 People Ticket Amount:{total} Rs")
print("*children Below (Age 12) 30% Discount & Senior Citizen Above (Age 59) 50% Discount*")