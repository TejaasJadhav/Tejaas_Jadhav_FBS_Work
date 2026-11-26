# 1 understand that every function is object of function class
#     a=10
#     print(type(a))
# def demo():
#     print(" ami i in demo")
#     print(type(demo))


# 2 we can store the funcction in Variable

# def demo():
#     print(" ami in in demo")
#     x=demo
#     demo()
#     x()

# 3 we can pass the function as an argument to another function

# def hi():
#     print("am i in hi")
# def innerhi(a):
#     print(a)
#     a()
#     innerhi(hi)

# 4 we can return a function from another function

# def demo1():
#     print(" am in demo1")
#     def innerfun():
#         print("am i in ineerfun")
#     return innerfun
# res=demo1()
# res()


# 5 closure

# def fun1(a):
#     print("first fun:",a)
#     def fun2():
#         print("second fun:",a)
#         return fun2
#     res=fun1(40000)
#     res()

#decorator -> wrapper


def decorator(a):
    print("in deco")
    def wrapper(*ar):
        print("time started")
        print('before calling')
        a(*ar)
        print("Time stoped")
        print("After Calling")
    return wrapper
@decorator  #res=dectorator(auth)
def auth():
    print("authentication is done")
auth()

@decorator
def sub(a,b):
    print(f"substraction={a-b}")
    sub(12,4)