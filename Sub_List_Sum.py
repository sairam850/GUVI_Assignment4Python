#Python Program to find Sublist Zero
my_list = [4,2,-3,1,6]
n = len(my_list)
#Initialise Empty Sublist
sublist = []
#Iteration through Loops
for i in range(0,n+1):
    for j in range(i+1,n+1):
        sublist.append(my_list[i:j])

for i in sublist:
    if sum(i) == 0:
        print(i)