a=5
for i in range(1,a+1):
    for j in range(a,a-i,-1):
        print(j,end=" ")
    print()