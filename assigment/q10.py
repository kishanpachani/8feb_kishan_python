"""
Write a python program that will return true if the two given integer
values are same or their sum or difference is 5.
"""
a=int(input("1st value :"))
b=int(input("2nd value :"))
c=a+b
d1=a-b
d2=b-a

if a==b or c==5:
    print(True)
elif d1==5 or d2==5:
    print(True)
else:
    print(False)
