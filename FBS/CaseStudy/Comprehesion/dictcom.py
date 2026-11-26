#    d={}
#   for i in range(11,26):
#        d[i]=i*i
#    print(d)

dic={i:i*i for i in range(11,26) if i%2!=0}
print(dic)