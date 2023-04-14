"""q.6 ) Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings."""


words=["awc","xyz","aba","1221","343","wow"]
count=0
for w in words:
    if len(w)>1 and w[0]==w[-1]:
        count+=1
print(count)