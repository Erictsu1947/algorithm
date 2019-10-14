
def bubble_sort_1(arr):
    length = len(arr)
    if length <= 1:
        return arr
    unsorted = length
    index = 0
    while index < unsorted - 1:
        if arr[index] > arr[index+1]:
            arr[index], arr[index+1] = arr[index+1], arr[index]
        index += 1
        if index == unsorted-1:
            index = 0
            unsorted -= 1
    return arr


def bubble_sort_2(arr):
    length = len(arr)
    if length <= 1:
        return arr
    for index in range(length):
        for i in range(1, length-index):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr


array = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(bubble_sort_1(array))
print(bubble_sort_2(array))
