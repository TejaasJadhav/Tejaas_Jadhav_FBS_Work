#Convert distant given in feet and inches into meter and centimeter.

feet_inches = float(input("Enter Distant in Feet & Inches :"))

meter = float(feet_inches*30.48/100)    #(12 inches = 1 feet , 1 inche = 2.54 cm , 12 iches = 30.48 cm)
centimeter = int(meter*100)

print(f"distant Given in feet and Inches into meter is :{meter}m & centimeter is :{centimeter}cm")