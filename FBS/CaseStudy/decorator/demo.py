def outerfun(a):
    print(" I am in decorator")
    def innerfun(*ar):
        print("Time Stopped")
        a(*ar)
        print("Time Stopped ")
    return innerfun
@outerfun
def login():
    print("login is done")
@outerfun
def logout():
    print("logout is done")
@outerfun
def add(a,b):
    print(a*b)

login()
logout()

