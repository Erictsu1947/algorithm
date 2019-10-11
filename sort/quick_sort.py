

class Solution:

    def __init__(self):
        pass

    def partition(self, nums, low, high):
        temp = nums[low]
        while low < high:
            while low < high and nums[high] > temp:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < temp:
                low += 1
            nums[high] = nums[low]
        nums[low] = temp
        return low

    def q_sort(self, nums: list, start: int, end: int):
        if start < end:
            pivot = self.partition(nums, start, end)
            self.q_sort(nums, start, pivot - 1)
            self.q_sort(nums, pivot + 1, end)
        return nums

    def quick_sort(self, nums):
        return self.q_sort(nums, 0, len(nums) - 1)


# nums = [3, 2, 1, 5, 6, 4]
# result = Solution().quick_sort(nums)
# print(result)

def swap(arr, m, n):
    arr[m], arr[n] = arr[n], arr[m]

# 用迭代的方式实现一个版本

def partition(arr, low, high):
    temp = arr[high]
    i = low - 1
    for j in range(low, high-1):
        if arr[j] < temp:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1


def q_sort(arr: list, start: int, end: int):
    if start < end:
        pivot = partition(arr, start, end)
        print(pivot)
        q_sort(arr, start, pivot - 1)
        q_sort(arr, pivot + 1, end)
    return arr


def quick_sort(arr):
    return q_sort(arr, 0, len(arr) - 1)


nums = [3, 2, 1, 5, 6, 4]
result = quick_sort(nums)
print(result)
