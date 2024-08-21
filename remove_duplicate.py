def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

numbers = [1, 2, 3, 2, 4, 5, 6, 2, 7, 8]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)