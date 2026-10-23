#if the output for the input returns true input will consider else not consider
# only filter true value

data=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda num: num%2==0,data))
print(res)

#res =list(filter(lambda num : num**2,data))
#print(res)