import collections

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hit_deque = collections.deque([])

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        start  = timestamp - 300
        queue = self.hit_deque
        
        while queue and queue[0] <= start:
            queue.popleft()
        queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start  = timestamp - 300
        queue = self.hit_deque
        
        while queue and queue[0] <= start:
            queue.popleft()
                
        
        return len(queue)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
