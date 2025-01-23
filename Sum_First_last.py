# First and Last Digit of Number

number = 12

# Assign the Last Digit to Result Variable
result = number%10

#Continue Loop until number becomes less than 9
while number>9:
    number = number//10

# Adding the number in Result Variable
result = result+number

#Display Output
print ("Result of First and last digit number is",result)