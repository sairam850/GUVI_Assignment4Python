# Minimum Elements in list

#Define a List
my_list = [5, 6, 1, 2, 3, 4]
result = my_list[0]

# Traverse over list to find minimum element
for i in range(1,len(my_list)):
    result = min(result,my_list[i]) 

#Print the Minimum Value in List
print("Minimum Value is", result)