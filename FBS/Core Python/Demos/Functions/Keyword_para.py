#keyword parameter

def employee(id,name,sal,dept):
    print("ID:",id)
    print("NAME:",name)
    print("SALARY:",sal)
    print("DEPT:",dept)
    print("#########")
employee(dept="back office",name="Tejaas",sal=20000,id=122)


#to neglact positonal para
#assign value to para in function call 
#name of para in function call and function definition sould be same
#flow form right to left (why: positional para flow is form left to right)