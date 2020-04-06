class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        m = len(A)
        if len(A) < 3:
            raise ValueError
            
        i_min, i_max, mid = 0, m - 1, m//2
        
        while i_min < i_max:
            
            mid = (i_min + i_max)//2
            
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                i_min = mid
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                i_max = mid
        
