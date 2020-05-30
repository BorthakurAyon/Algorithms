from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        ans = ''
        
        ds = Counter(s)
        bucket = defaultdict(list)
        
        for key, value in ds.items():
            bucket[value].append(key)
        
        
        for i in range(n, 0, -1):
            if len(bucket[i]):
                for item in bucket[i]:
                    ans += i * item
        
        return ans
                
        
