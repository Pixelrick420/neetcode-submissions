class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        profit = 0

        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        
        return profit

