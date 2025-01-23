# Duplicate Items in List

#Declare Lists
my_list1 = [1,2,2,3,4]
my_list2 = [3,4,5,5]
my_list3 = [3,6,6]

#Combine Lists
my_list1.extend(my_list2)
my_list1.extend(my_list3)

#Create a empty List to store values
dup_items = []
non_dup = []

# Iterate through each value in the list 'my_list'
for i in my_list1:
    # Check if the value is not already in 'res'
    if i not in non_dup:
        non_dup.append(i)
    elif i not in dup_items:
        dup_items.append(i)


print(dup_items)