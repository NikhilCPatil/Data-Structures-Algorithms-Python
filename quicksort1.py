"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partation(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)


def quicks(array, low, high):
    if low < high:
        pi = partation(array, low, high)
        quicks(array, low, pi - 1)
        quicks(array, pi + 1, high)


def quicksort(array):
    quicks(array, 0, len(array) - 1)
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))
