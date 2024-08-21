def fizzBuzz(elements):
    for i, num in enumerate(elements):
        if num % 3 == 0 and num % 5 == 0:
            elements[i] = "FizzBuzz"
        elif num % 3 == 0:
            elements[i] = "Fizz"
        elif num % 5 == 0:
            elements[i] = "Buzz"


numbers = [45, 22, 14, 15, 20, 30, 40]
fizzBuzz(numbers)
print(numbers)
