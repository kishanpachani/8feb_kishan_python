# Write a Python program to get unique values from a list

lst=[2,3,7,7,7,2,2,8,9,10,8]
uniq_lst=[]
for x in lst:
    if x not in uniq_lst:
        uniq_lst.append(x)
print(uniq_lst)