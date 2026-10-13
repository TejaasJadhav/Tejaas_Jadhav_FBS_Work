# A->65,B-66 ----Z-
# a-96 
count=65
for  row in range(1,5):
    for column in range(1,5):
        print(chr(count),end="  ")
        count+=1
    print()