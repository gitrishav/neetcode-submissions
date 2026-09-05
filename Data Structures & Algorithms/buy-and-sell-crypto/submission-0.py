class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0  # Buy pointer
        right = 1 # Sell pointer
        max_profit = 0

        while right < len(prices):
            # If profitable, calculate and potentially update max_profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # If we find a new, lower price, shift our buy pointer to it
                left = right
            
            # Move to the next day
            right += 1

        return max_profit