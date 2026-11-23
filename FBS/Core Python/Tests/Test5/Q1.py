    #A list contains the denominations as follows :
    #D = [2000, 500, 200, 100 , 50, 20, 10, 5]
    #Accept an amount from user and calculate how many
    #minimum number of notes will be needed for that
    #amount.


D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))

if amount % 5 != 0:
    print("Amount must be a multiple of 5 (smallest note is 5).")
else:
    counts = []          # counts[i] = number of notes of D[i]
    total_notes = 0
    remaining = amount

    for note in D:
        n = remaining // note
        counts.append(n)
        total_notes += n
        remaining %= note

    print("\nNote breakdown:")
    for i in range(len(D)):
        if counts[i] > 0:
            print(f"{D[i]} x {counts[i]}")

    print("Minimum number of notes:", total_notes)