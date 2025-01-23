# Prime Number and Counting 

#Define a List
list_numbers = [10,501,22,37,100,999,87,351]

#Create empty list and Prime count
prime = []


#Find Prime Number and Count
for i in list_numbers:
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count = count+1
    if count == 1:
        prime.append(i)

print(prime)
print(len(prime))
