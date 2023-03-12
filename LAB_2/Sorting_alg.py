import numpy as np
import matplotlib.pyplot as plt
import timeit
import random as rnd


# Selection Sort
def selectionSort(arr):
    for i in range(len(arr)):

        # Find the minimum element in remaining
        minPosition = i

        for j in range(i + 1, len(arr)):
            if arr[minPosition] > arr[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        temp = arr[i]
        arr[i] = arr[minPosition]
        arr[minPosition] = temp


# Merge Sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Heap sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# Quick Sort
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


sorts = [
    # {
    #     "name": "Selection Sort",
    #     "sort": lambda arr: selectionSort(arr)
    # },
    {
        "name": "Merge Sort",
        "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
    },
    {
        "name": "Quick Sort",
        "sort": lambda arr: quickSort(arr, 0, len(arr) - 1)
    },
    {
        "name": "Heap Sort",
        "sort": lambda arr: heap_sort(arr)
    }
]

elements = np.array([i * 1000 for i in range(1, 50)])

plt.xlabel('List Length')
plt.ylabel('Time Complexity (s)')

for sort in sorts:
    times = list()
    start_all = timeit.default_timer()
    for i in range(1, 50):
        start = timeit.default_timer()
        a = np.random.randint(10000, size=i * 1000) 
        sort["sort"](a)
        end = timeit.default_timer()
        times.append(end - start)

        print(sort["name"], "Sorted", i * 1000, "Elements in", end - start, "s")
    end_all = timeit.default_timer()
    print(sort["name"], "Sorted Elements in", end_all - start_all, "s")

    plt.plot(elements, times, label=sort["name"])

plt.grid()
plt.legend()
plt.show()
