# Heap Sort Algo

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


def heap_sort_basic(arr):
    n = len(arr)

    # max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


num = [12, 11, 13, 5, 6, 7]
print(heap_sort_basic(num))

# Heap Sort Algo Optimised 

def heapify_iterative(arr, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heap_sort_optimized(arr):
    n = len(arr)

    # build max heap (bottom-up)
    for i in range(n // 2 - 1, -1, -1):
        heapify_iterative(arr, n, i)

    # extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_iterative(arr, i, 0)

    return arr

print(heap_sort_optimized(num))

# Hemant Thapa @ 2026
