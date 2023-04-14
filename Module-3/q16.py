list = ['a','x',[1,3,5,6,'zalak']]
for i in list:
    if len(i) > 1:
        print("sublist is present in list")
        break
else:
    print("sublist is not present in list")