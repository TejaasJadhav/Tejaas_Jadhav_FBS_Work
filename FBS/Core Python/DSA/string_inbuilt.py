#s="fristbit solutions"
#s2=s.upper()
#print(s2)
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.title())
#s="PytHon"
#print(s.swapcase())


#s='pyhton programming'
#print(s.find('p'))
#print(s.find('prrogram'))
#print(s.find("Java"))
#print(s.index("85"))
#print(s.count("2"))
#print(s.startswith("python"))
#print(s.endswith("ing9"))

s="  Python"
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s="am!i!good!at!python"
s2=s.split("!")
print(s2)

r="-".join(s2)
print(r)

a="Abcd"
print(a.isalpha())
b="abc1234"
print(b.isalnum())
c="12122hjs"
print(c.isnumeric())