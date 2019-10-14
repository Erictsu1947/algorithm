class Solution:
    def maxProfit_1(self, prices) -> int:
        length = len(prices)
        dp = [0 for _ in range(length)]
        for i in range(length):
            for j in range(i, length):
                dp[i] = max(dp[i], prices[j]-prices[i])
        return max(dp)

    def maxProfit(self, prices) -> int:
        length = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(length):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i]-min_price, max_profit)
        return max_profit


prices = [7,1,5,3,6,4]

# prices = [7,6,4,3,1]

print(Solution().maxProfit(prices))