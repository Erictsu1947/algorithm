class Solution:

    def partition_1(self, nums, l, h):
        temp = nums[h]
        i = l - 1
        for j in range(l, h-1):
            if nums[j] < temp:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        if nums[i+1] < nums[h]:
            nums[i+1], nums[h] = temp, nums[i+1]
        return l

    def partition(self, nums, l, h):
        temp = nums[l]
        while l < h:
            while l < h and nums[h] > temp:
                h -= 1
            while l < h and nums[l] < temp:
                l += 1
            nums[l], nums[h] = nums[h], nums[l]
        nums[l] = temp
        return l

    def findKthLargest(self, nums, k: int) -> int:
        pivot = self.partition(nums, 0, len(nums) - 1)

        length = len(nums)
        while True:
            rank = length - pivot
            print(nums, rank)
            if rank > k:
                pivot = self.partition(nums, pivot + 1, length - 1)
            elif rank < k:
                pivot = self.partition(nums, 0, pivot - 1)
            else:
                return nums[pivot]


nums = [3, 2, 1, 5, 6, 4]
k = 4

# nums = [4, 4]
# k = 2


print(Solution().findKthLargest(nums, k))
