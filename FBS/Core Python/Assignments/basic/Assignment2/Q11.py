#Write a program to accept an integer amount from user and tell minimum
          #number of notes needed for representing that amount.

amount=int(input("Enter the Amount :"))

n2000 = amount//2000
remain_note = amount%2000

n500 = remain_note//500
remain_notehundred = remain_note%500

n100 = remain_notehundred//100
remain_notefifty = remain_notehundred%100

n50 = remain_notefifty//50
remain_notetwenty = remain_notefifty%50

n20 = remain_notetwenty//20
reamin_noteten = remain_notetwenty%20

n10 = reamin_noteten//10

print(f"Amount Has :{n2000} 2 Thousand Note")
print(f"Amount Has :{n500} 5 Hundred Note")
print(f"Amount Has :{n100} 1 Hundred Note")
print(f"Amount Has :{n50} Fifty Note")
print(f"Amount Has :{n20} Twenty Note")
print(f"Amount Has :{n10} Ten Note")