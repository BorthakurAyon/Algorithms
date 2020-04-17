class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        sums = [0]
        for idx, val in enumerate(nums):
            sums.append(sums[idx] + val)
        
        F = [[float("inf") for _ in range(m+1)] for _ in range(n+1)]
        for l in range(1, n+1):
            F[l][1] = sums[l]
        
        for l in range(1, n + 1):
            for k in range(1, m + 1):
                for j in range(l):
                    F[l][k] = min(F[l][k], max(F[j][k-1], sums[l]-sums[j]))
                    
        return F[n][m]
