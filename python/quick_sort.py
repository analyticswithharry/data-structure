# Quick Sort Algo

def quicksort_basic(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # weak choice
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return quicksort_basic(left) + [pivot] + quicksort_basic(right)


num = [10, 7, 8, 9, 1, 5]
print(quicksort_basic(num))

# Quick Sort Optimised Algo
def quicksort_optimized(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_optimized(arr, low, pivot_index - 1)
        quicksort_optimized(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]  # better pivot
    i = low
    j = high

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i - 1

print(quicksort_optimized(num))

# Hemant Thapa @ 2026
