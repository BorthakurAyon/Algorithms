class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        
        if n < 2:
            return 0
        
        buy, sell = [float("inf")] * n, [0] * n
        
        for i in range(n):
            
            buy[i] = max((buy[i-1] if i > 0 else - prices[0]), (sell[i-2] if i > 1 else 0) - prices[i])
            sell[i] = max((sell[i - 1] if i > 0 else 0), (buy[i-1] if i > 0 else -prices[0]) + prices[i])
        return sell[-1]
