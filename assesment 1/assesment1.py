f1=open("kishan patel.txt","a")

print(" ***welcom to  my fruit market ****")

print(" 1) manager ?  \n 2) costmer ?")

mymarket = int(input("please select your role : ? "))

if mymarket==1:

 print("+   * fruit market manager *  +")
elif mymarket==2:
 print("+   * fruit market costmer *  +")
else:
 print("1) add fruit stock \n2) view fruit stock \n3) update fruit stock")


mymarket = input ("please select your choice : ? ")

fruit=input("enter fruit name \n:")

f1.write("add fruit stock \n")
f1.write(f'{fruit}\n')
kg=input("enter qty (in kg) :\n")
f1.write(f'{kg}\n')
f1.write("enter price :100 \n")


