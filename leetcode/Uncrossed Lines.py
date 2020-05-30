class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        m, n = len(A), len(B)
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        if A[0] == B[0]:
            dp[0][0] = 1 
    
    
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            
            if A[0]==B[i]:
                dp[i][0] = 1
                
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1]

            if A[i]==B[0]:
                dp[0][i] = 1
                
        for i in range(1, n):
            for j in range(1, m):
                
                dp[i][j] = max(int(A[j] == B[i]) + dp[i - 1][j - 1], dp[i-1][j], dp[i][j-1])
        
        
        return dp[n - 1][m - 1]
