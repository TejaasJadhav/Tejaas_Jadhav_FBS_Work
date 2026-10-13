# A->65,B-66 ----Z-
# a-96 
count=65
for  row in range(1,5):
    for column in range(1,5):
        print(chr(count),end="  ")
        count+=1
    print()

#for i in range(65,69):
#    for j in range(1,5):
#       print(chr(i),end=" ")
#  print()

#output :
# A A A A
# B B B B 
# C C C C
# D D D D 