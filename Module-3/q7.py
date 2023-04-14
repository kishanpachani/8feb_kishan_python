# 7) Write a Python program to remove duplicates from a list.

lst=[2,3,7,7,7,2,2,8,9,10,8,10]
newlst=[]
for data in lst:
    if data not in newlst:
        newlst.append(data)
print(newlst)