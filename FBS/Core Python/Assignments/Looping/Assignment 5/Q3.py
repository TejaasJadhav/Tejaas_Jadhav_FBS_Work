#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n = int(input("Enter Number of Passengers :"))
ticket=int(input("Enter Ticket Price : "))
total=0
for passenger in range(1,n+1):
    age=int(input(f"Enter Age of passenger {passenger} "))
    if(age<12):
            fare=ticket*0.70
            print("Children Below 12 30% Discount Applied")
    elif(age>59):
            fare=ticket*0.50
            print("Senior Citizen Above 59 50% Discount Applied")
    else:
            fare=ticket
    total+=fare
print(f"Total Amount of all Passenger is {total}")
