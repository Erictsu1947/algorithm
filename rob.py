class Solution:
    def rob(self, nums) -> int:
        """
        f[n] = max(f[n-2]+nums[n], f[n-1])
        """
        if not nums:
            return 0

        dp = [nums[0], max(nums[0], nums[1])]
        length = len(nums)
        for i in range(2, length):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        return max(dp)


nums = [2,7,9,3,1]
print(Solution().rob(nums))