import itertools

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        lastnum = lower - 1
        res = []
        
        for num in itertools.chain(nums, [upper + 1]):
            
            if lastnum + 2 == num:
                res.append(str(lastnum + 1))
            elif lastnum + 2 < num:
                res.append(("{}->{}").format(lastnum +1, num - 1))
            
            lastnum = num
            
        return res
                
