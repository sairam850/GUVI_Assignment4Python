# Sum Triplets

#Python Program to find Sublist Zero
my_list = [10,20,30,9]
n = len(my_list)
#Initialise Empty Sublist
sublist = []
#Iteration through Loops
for i in range(0,n+1):
    for j in range(i+1,n+1):
        sublist.append(my_list[i:j])

for i in sublist:
    if sum(i) == 59:
        print(i)


