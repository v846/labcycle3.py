my_list = [(43, 15), (66, 98), (64, 80), (14, 9), (47, 17)]

print("The list is : ")
print(my_list)

my_result = []
for sub in my_list:
   if my_result and my_result[-1][0] == sub[0]:
      my_result[-1].extend(sub[1:])
   else:
      my_result.append([ele for ele in sub])
my_result = list(map(tuple, my_result))

print("The extracted elements are : " )
print(my_result)
