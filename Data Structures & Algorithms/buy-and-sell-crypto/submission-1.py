class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = 0, 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] < prices[buy]:
                buy = i
            else:
                profit = max(profit, prices[i] - prices[buy])
        return profit