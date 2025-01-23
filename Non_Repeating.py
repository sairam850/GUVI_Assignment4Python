# Python3 program to find first
# non-repeating element.
 
 
def firstNonRepeating(my_list, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in my_lis
        while(j < n):
            if (i != j and my_list[i] == my_list[j]):
                break
            j += 1
        # if ith element is not present in my_list
        # except at ith index then return element
        if (j == n):
            return my_list[i]
 
    return -1
 
 
# Driver code
my_list = [9, 4, 9, 6, 7, 4]
n = len(my_list)
print(firstNonRepeating(my_list, n))