class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        ans = set()
        n = len(nums)
        for x, val in enumerate(nums):
            for y in range(x + 1, n + 1):
                ans.add(frozenset(nums[x:y]))
                for u in range(0, x + 1):
                    for z in range(y + 1, n + 1):
                    
                        ans.add(frozenset([nums[u]] + nums[y:z + 1]))
                        ans.add(frozenset(nums[0:u + 1] + nums[y:z + 1]))

                        ans.add(frozenset([nums[u]] + nums[z:n + 1]))
                        ans.add(frozenset(nums[0:u + 1] + nums[z:n + 1]))
    
        ans.add(frozenset([]))
        return ans
        '''
        
        all_subsets = [[]]
        
        if nums:
            
            for num in nums:
                for idx in range(len(all_subsets)):
                    
                    all_subsets.append(all_subsets[idx] + [num])
            
            
        return all_subsets
