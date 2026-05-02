# normal bubble sort algo
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

num = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(num))

# optimised normal bubble sort algo
def bubble_sort_optimized(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

print(bubble_sort_optimized(num))

# Hemant Thapa @ 2026
