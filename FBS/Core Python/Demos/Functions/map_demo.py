#method 1
#def sq(n):
#    return n**2
data=[1,2,3,4,5,6,7,8,9,10]
#res=list(map(sq, data))
#print(res)

#method 2

res=list(map(lambda n: n**2,data))
print(res)