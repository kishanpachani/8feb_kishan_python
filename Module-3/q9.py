def comman_data(list1,list2):
     result = False
     for x in list1:

           for y in list2:

               if x == y:
                  result = True
                  return result

a = [x for x in input("enter list1 :").split()]
b = [x for x in input("enter list2 :").split()]
print(comman_data(a,b))
         