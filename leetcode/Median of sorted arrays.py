import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        
        if not m and n: return None
        
        if not m:
            if n % 2:
                return nums2[int(n+1)/2]
            else:
                return (num2[int(n/2)] + nums[int((n/2) + 1)])/2
            
        
        
        
       
