
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


nums = [3, 2, 1, 5, 6, 4]
result = Solution().quick_sort(nums)
print(result)
