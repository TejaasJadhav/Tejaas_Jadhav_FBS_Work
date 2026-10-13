#Convert the time entered in hh,min and sec into seconds.

Hours = int(input("Enter Hours: "))
Minutes = int(input("Enter Minutes: "))
Seconds = int(input("Enter Seconds: "))
#operations
h = int(Hours*3600)
m = int(Minutes*60)
s = int(Seconds*1)

final_answer = h+m+s
print(f"Total Hours,Minutes & Seconds Contain :{final_answer} seconds")

print(id(s))
print(id(Seconds))