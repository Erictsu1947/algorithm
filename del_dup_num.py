class Solution:

    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        length = len(nums)
        index = 0
        while index < length - 1:
            temp = nums[index]
            if nums[index + 1] == temp:
                nums.pop(index + 1)
                length -= 1
            else:
                index += 1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
print(nums)