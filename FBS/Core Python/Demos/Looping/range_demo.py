##Range 
#    Range(Start,stop,step)


#      2 table = (2,21,2)
#      5 table = (5,51,5)


n = 5
#for i in range(n,n*10+1,n):       #for number any table 

#for i in range(n*10,n-1,-n):     #reverse Table for any number


#      1-10   numbers display = (1,11,1)
#for i in range(1,11):
    #print(i)


#for r in range(5):     #when you give single number it start from 0 to (5) end
   # print(r)


n = int(input("Enter Number to Get Sum of Series"))
sum =0
for i in range(1,n+1):
    sum+=i  #sum=sum+i
print(f"Addition :", sum)
