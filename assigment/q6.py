"""Write a python program that swap two numbers with temp variable and 
without temp variable"""

a=int(input("enter velue of a :"))  
b=int(input("enter value of b :"))

c=a    # Swaping value of two variables with the help of a temporary variable
a=b
b=c
print("value of a:",a)
print("value of b:",b)


a=43
b=55
a,b=b,a         # Swaping value of two variables without using a temporary variable
print("Value of A:", a)
print("value of B:",b)