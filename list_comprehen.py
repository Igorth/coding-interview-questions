def square(x):
    return x ** 2


def is_odd(x):
    return bool(x % 2)


numbers = [2, 3, 4, 5, 6, 7, 8]


# FILTER AND LIST COMPREHENSIONS
print(list(filter(is_odd, numbers)))
odd_numbers = [num for num in numbers if is_odd(num)]
print(odd_numbers)

# MAP and LIST COMPREHENSIONS
print(list(map(square, numbers)))
square_numbers = [square(num) for num in numbers]
print(square_numbers)



