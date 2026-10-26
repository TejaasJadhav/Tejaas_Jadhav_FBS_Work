#Write a program to accept distance in km and convert it into meters and
#centimeters both.

km = float(input("Enter Distance in Kilometers : "))
meters = float(km*1000)
centimeters = float(km*10000)

print(f" km into meters {meters} m & centimeters {centimeters} cm")