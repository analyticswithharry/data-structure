def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # assume current index has minimum value
        min_index = i

        # find smaller element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap current element with minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


numbers = [64, 25, 12, 22, 11]

sorted_numbers = selection_sort(numbers)

print("Sorted Array:", sorted_numbers)
