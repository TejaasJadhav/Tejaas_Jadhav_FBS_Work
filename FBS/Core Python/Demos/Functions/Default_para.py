#Default parameter

#1 to make parameter optional
#2 Assign Value to para in function definition

def emp(id,name,sal,dept="Back Office"):
    print("ID:",id)
    print("NAME:",name)
    print("SALARY:",sal)
    print("DEPT:",dept)
    print("###########")
emp(101,"Tejas",10000,"IT")
emp(102,"OM",50000)

#3 if we passed value to default para in function call it takes passed value if we dont pass value to default
# para it takes default value
#4 flow is form right to left

def emp(id,name,sal=15000,dept="Back Office"):
    print("ID:",id)
    print("NAME:",name)
    print("SALARY:",sal)
    print("DEPT:",dept)
    print("###########")
emp(101,"Tejas")