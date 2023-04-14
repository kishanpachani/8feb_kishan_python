from collections import Counter
my_dict = {'t': 3, 'u': 4, 't': 6, 'o': 5, 'r': 21}
k = Counter(my_dict)
high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for i in high:
   print(i[0]," :",i[1]," ")