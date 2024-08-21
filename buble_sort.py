def bubble_sort(elements):
    n = len(elements)
    for i in range(n):
        for j in range(0, n - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

numbers = [5, 2, 3, 9, 10]
bubble_sort(numbers)
print(numbers)