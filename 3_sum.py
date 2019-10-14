class Solution:
    def threeSum(self, nums):
        if not nums:
            return []

        nums.sort()
        result = []
        length = len(nums)
        for idx, item in enumerate(nums[:-2]):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            l, r = idx + 1, length - 1
            while l < r:
                s = item + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([item, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result

# nums = [-1, 0, 1, 2, -1, -4]
nums = [-2,0,0,2,2]
print(Solution().threeSum(nums))
