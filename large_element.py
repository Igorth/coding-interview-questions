def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest


nums = [10, 20, 30, 132, 50, 60]
largest_num = find_largest(nums)
print(f"The largest number is: {largest_num}")
