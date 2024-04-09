from random import randint

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        split_index = partition(arr, low, high)
        quick_sort(arr, low, split_index)
        quick_sort(arr, split_index + 1, high)

arr = [-2, 4, 8, 0, -3, 4, 11]
quick_sort(arr, 0, len(arr) - 1)
print(*arr)
    
