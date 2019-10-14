
def swap(arr, m, n):
    arr[m], arr[n] = arr[n], arr[m]

# 用迭代的方式实现一个版本

def partition(arr, low, high):
    print(arr, low, high)
    temp = arr[high]
    i = low - 1
    for j in range(low, high-1):
        if arr[j] < temp:
            i += 1
            swap(arr, i, j)
    if arr[i+1] > temp:
        swap(arr, i+1, high)
    return i+1


def q_sort(arr: list, start: int, end: int):
    if start < end:
        pivot = partition(arr, start, end)
        q_sort(arr, start, pivot - 1)
        q_sort(arr, pivot + 1, end)
    return arr


def quick_sort(arr):
    return q_sort(arr, 0, len(arr) - 1)


nums = [3, 2, 1, 5, 6, 4]
result = quick_sort(nums)
print(result)
