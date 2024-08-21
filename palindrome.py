def is_palindrome(my_string):
    reversed_string = my_string[::-1]
    return reversed_string == my_string


word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    