# 基本二分查找
def binary_search(arr, target):
    count = 0
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2
        if target > arr[mid]:
            l = mid
        elif target < arr[mid]:
            r = mid
        else:
            return mid
        count += 1
        print(count)


nums = range(1000)
result = binary_search(nums, 520)
print(result)
