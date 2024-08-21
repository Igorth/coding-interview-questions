# One line anonymous function
def identify(x):
    return x

lambda x: x

# The keyword: lambda
# A bound variable: x
# A body: x

add_one = lambda x: x + 1
print(add_one(2))

def add_one(x):
    return x + 1

# A lambda function can have multiple arguments
multiply = lambda x, y: x * y
print(multiply(2, 3))

full_name = lambda first, last: f"Full Name: {first} {last}"
print(full_name("joj", "joj"))


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def square(x):
    return x ** 2


square_li = list(map(lambda x: x ** 2, my_numbers))
print(square_li)

evens = list(filter(lambda x: x % 2 == 0, my_numbers))
print(evens)

values = [(1, 'b', 'hell'), (2, 'c', 'ell'), (3, 'a', 'ok')]
print(type(values))
sorted_values = sorted(values, key=lambda x: x[1])
print(sorted_values)

#----------------------------------------------------------------
from functools import reduce

number_s = [1, 2, 3, 4, 5, 6, 7]

# Using reduce to sum the list without initializer
# acc -> 1
# x -> 2
sum_of_numbers = reduce(lambda acc, x: acc + x, number_s)
print(sum_of_numbers)
