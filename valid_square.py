def valid_square(number):
    square = int(number ** 0.5)
    check = square ** 2 == number
    return check

# Test the function
print(valid_square(16))  # True
print(valid_square(10))  # False