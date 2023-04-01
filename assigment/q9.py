"""Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero."""


a=int(input("Enter 1st value :"))
b=int(input("Enter 2nd value "))
c=int(input("Enter 3rd value :"))

if a==b or a==c or c==b:
    print("The sum is zero")
else:
    print(a+b+c)