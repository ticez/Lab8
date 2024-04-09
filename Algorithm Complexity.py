import timeit
import memory_profiler
from cpuinfo import get_cpu_info
from random import randint


@memory_profiler.profile
def sort(arr):
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                count += 1
    return arr, count


k = get_cpu_info()['l3_cache_size'] // 1024 // 1024

min_size = k * 2
step = k * 2
max_size = k * 20

for i in range(min_size, max_size + 1, step):
    arr = [randint(1, 50) for x in range(i)]
    time_start = timeit.default_timer()
    arr, count = sort(arr)
    time_end = timeit.default_timer()
    print(f"Время выполения: {time_end - time_start}")
    print(f"Кол-во операций: {count}")
    print(arr)
