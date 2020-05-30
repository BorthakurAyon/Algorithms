'''
class StockSpanner:

    def __init__(self):
        
        self.price_list = []

    def next(self, price: int) -> int:
        
        span = 0
        if not price: return
        self.price_list.insert(0, price)
        for item in self.price_list:
            if item > price:
                break
            else:
                span += 1
        
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''

class StockSpanner:

    def __init__(self):
        
        self.price_list = []

    def next(self, price: int) -> int:
        
        span = 1
        
        while self.price_list and self.price_list[-1][0] <= price:
            span += self.price_list.pop()[1]
        self.price_list.append((price, span))
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
