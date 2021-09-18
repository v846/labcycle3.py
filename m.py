my_str = 'Jane is the best . Jane loves to cook. Jane and Will cook together'
print("The string is : ")
print(my_str)
replace_dict = {'Jane' : 'She' }
my_list = my_str.split(' ')
my_result = ' '.join([replace_dict.get(val) if val in replace_dict.keys() and my_list.index(val) != idx else val for idx, val in enumerate(my_list)])
print("The string after replacing with values is : ")
print(my_result)
