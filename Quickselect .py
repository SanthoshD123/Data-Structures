import random

def quickselect(arr, k):
    k = len(arr) - k  
    left, right = 0, len(arr) - 1

    while left <= right:
        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        arr[store_index], arr[right] = arr[right], arr[store_index]

        if store_index == k:
            return arr[store_index]
        elif store_index < k:
            left = store_index + 1
        else:
            right = store_index - 1

arr = [3, 2, 1, 5, 6, 4]
k = 3
print(quickselect(arr, k))  
