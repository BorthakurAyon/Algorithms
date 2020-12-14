class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            
            return 0
        
        print(prices)
        
        max_profit = 0
        max_selling_price = prices[-1]
        
        
        for item in prices[:-1][::-1]:
            
            if max_selling_price - item > max_profit:
                max_profit = max_selling_price - item
                
            max_selling_price = max(max_selling_price, item)
        
        return max_profit
