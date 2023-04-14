# Write a Python program to calculate surface volume and area of a cylinder

pi=22/7
height=float(input("height of cylinder:"))
radian=float(input("radius of cyilnder:"))
volume=pi*radian*radian*height
sur_area=((2*pi*radian)*height+(pi*radian**2)*2)
print(volume)
print(sur_area)