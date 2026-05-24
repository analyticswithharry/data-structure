# linear_search.py

def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]

target = 40

result = linear_search(numbers, target)

print("Index:", result)
