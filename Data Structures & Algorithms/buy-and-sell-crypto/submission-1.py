class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                current = prices[sell] - prices[buy]
                profit = max(profit, current)
            else:
                buy = sell
            sell += 1        
        return profit
                        
