###Numeric
 
#1. int 
a = 10

#2. float
b = 3.14

#3. Complex
x = 10 + 5j  #real + Imaginary
print(x,type(x))                               #there are not Multi line comments in python
print(a,type(a))                           #(#) is used for single line comments in python
print(b,type(b))  


###Text 
#1. str

e='Tejas Jadhav'
e="Tejas jadhav"
e='''This is first line 
this is second line'''
e="""This is 1 line
this is 2 line"""
print(e,type(e))

###Sequential 
#1. list
l=[1,2,3,4,5]
print(l,type(l))

#2. tuple
t=(1,2,3,4,5)
print(t,type(t))

#3. range
r=range(10)
print(r,type(r))

##Set Type
#1. set
s={1,2,3,4,5}
print(s,type(s))

#2. frozenset
fs=frozenset({1,2,3,4,5})
print(fs,type(fs))

###mapping
#1. dict
d= {'id':101, 'name':'Tejas Jadhav'}
print(d,type(d))

###other
#1. Boolean
k=True
print(k,type(k))

#2 Nonetype
n=None
print(n,type(n))