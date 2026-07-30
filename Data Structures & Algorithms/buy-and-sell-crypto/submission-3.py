class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        n = len(prices)

        for i in range(1, n):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
            
        return profit