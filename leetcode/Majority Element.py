from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = -1
        num_cnt = defaultdict(int)
        for item in nums:
            num_cnt[item] += 1
            if num_cnt[item] > n/2 and num_cnt[item] > ans:
                ans = item
                
        return ans
