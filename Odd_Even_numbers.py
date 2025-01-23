#Odd and Even Numbers

#Define a List
list_numbers = [10,501,22,37,100,999,87,351]

#Create Empty list for odd and Even bucket
odd_bucket = []
even_bucket = []

#Separate list using Loops
for i in list_numbers:
    if(i%2 == 0):
        even_bucket.append(i)
    else:
        odd_bucket.append(i)

#Print odd and Even Bucket
print(odd_bucket)
print(even_bucket)