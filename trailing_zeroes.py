# Given an integer n, return the number of trailing zeroes in n factorial n!
def factorial_trailing_zeroes(n):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    print(fact)
    print(str(fact)[::-1])

    result = 0
    for i in str(fact)[::-1]:
        if i == '0':
            result += 1
        else:
            break
    return result


print(factorial_trailing_zeroes(10))
print(factorial_trailing_zeroes(18))
