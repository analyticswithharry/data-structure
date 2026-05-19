def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # move elements greater than key
        # one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insert key at correct position
        arr[j + 1] = key

    return arr


numbers = [64, 34, 25, 12, 22, 11, 90]

sorted_numbers = insertion_sort(numbers)

print("Sorted Array:", sorted_numbers)
