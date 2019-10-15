
def partition_1(arr, l, h):
    temp = arr[l]
    while l < h:
        while l < h and arr[h] > temp:
            h -= 1
        arr[l] = arr[h]
        while l < h and arr[l] <= temp:
            l += 1
        arr[h] = arr[l]
    arr[l] = temp
    return l


def partition(arr, l, h):
    temp = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] < temp:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[h], arr[i+1] = arr[i+1], arr[h]
    return i+1


def quick_sort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quick_sort(arr, l, pivot - 1)
        quick_sort(arr, pivot + 1, h)
    return arr


nums = [3, 2, 3, 1, 8, 5, 6, 4]
result = quick_sort(nums, 0, len(nums)-1)
print(result)
