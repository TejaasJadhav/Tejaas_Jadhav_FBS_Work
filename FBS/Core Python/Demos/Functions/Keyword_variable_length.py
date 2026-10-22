#1 to pass multiple values with Meaning
#2 Mention 2 asterick symbol before parameter name in function definition
#3 Values and Meaning are stored in dictionary
#4 To get key and Values Use for loop on dict.items()

def emp(**data):
    for key, val in data.items():
        print(key,":",val)
emp(id=101,name="Tejaas",age=21,sal=20000)