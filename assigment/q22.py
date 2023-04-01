inputString = "hello world"
 
count = 0
 
for i in inputString:
      count = count + 1
newString = inputString[ 0:2 ] + inputString [count - 2: count ]
 
print("Input string = " + inputString)
print("New String = "+ newString)