import math

def shellSort(arr):
    n = len(arr)
    k = int(math.log2(n))
    step = 2 ** k - 1
    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
        k -= 1
        step = 2 ** k - 1

arr = [21, 4, -7, 11, -3, 9]
shellSort(arr)
print(*arr)
