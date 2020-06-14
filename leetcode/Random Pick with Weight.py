import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        
        self._prefix_sum = list(w)
        for i in range(1, len(w)):
            self._prefix_sum[i] += self._prefix_sum[i-1]
        

    def pickIndex(self) -> int:
        
        target = random.randint(0, self._prefix_sum[-1] - 1)
        return bisect.bisect_right(self._prefix_sum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
