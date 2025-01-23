# Happy Numbers
def is_happy_number(n):
    seen = []  # Create an Empty List
    while n != 1 and n not in seen:
        seen.append(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Given Range of List Numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Check for happy numbers in the list
happy_numbers = [num for num in numbers if is_happy_number(num)]

print(f"Happy numbers from the list: {happy_numbers}")
print(len(happy_numbers))
