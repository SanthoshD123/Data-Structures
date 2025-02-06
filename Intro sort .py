import sys
from heapq import heappop, heappush

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, depth_limit):
    while low < high:
        if high - low < 16:
            insertion_sort(arr, low, high)
            break
        elif depth_limit == 0:
            heap_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                quick_sort(arr, low, pivot - 1, depth_limit - 1)
                low = pivot + 1
            else:
                quick_sort(arr, pivot + 1, high, depth_limit - 1)
                high = pivot - 1

def heap_sort(arr, low, high):
    heap = []
    for i in range(low, high + 1):
        heappush(heap, arr[i])
    for i in range(low, high + 1):
        arr[i] = heappop(heap)

def introsort(arr):
    depth_limit = 2 * (len(arr).bit_length() - 1)
    quick_sort(arr, 0, len(arr) - 1, depth_limit)
    return arr

arr = [10, 3, 2, 8, 15, 23, 7, 5]
print(introsort(arr))
