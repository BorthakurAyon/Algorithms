from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        cnt = collections.Counter(tasks)
        tmax = max(cnt.values())
        slots = (tmax - 1) * n
        tsum = len(tasks)
        return tsum + max(0, slots + tmax - 1 - sum(n - (n == tmax) for n in cnt.values()))
