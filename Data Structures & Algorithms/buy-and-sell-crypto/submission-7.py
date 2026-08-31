class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        for i in range(len(prices)-1):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            r += 1
            if profit < 0:
                l = r - 1
        return maxProfit