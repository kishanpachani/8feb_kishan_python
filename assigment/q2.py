#Write a python program to get a Factorial number of a given number.

number=int(input("Enter any number "))

factorial=1

if number<0:
    print("Error : Factorial of a negative number is not defined")
elif number==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print(factorial)