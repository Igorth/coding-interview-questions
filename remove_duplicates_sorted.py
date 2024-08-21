def removeDuplicates(my_array):
    size = len(my_array)
    insert_index = 1
    for i in range(1, size):
        if my_array[i - 1] != my_array[i]:
            my_array[insert_index] = my_array[i]
            insert_index += 1
    return insert_index


array_1 = [1, 2, 2, 3, 3, 4]
print(removeDuplicates(array_1))

array_2 = [1, 1, 3, 4, 5, 6, 6]
print(removeDuplicates(array_2))
