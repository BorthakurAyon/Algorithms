class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        num_path = [[0 for _ in range(n)] for _ in range(m)]
        
        num_path[-1][-1] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m-1, -1, -1):
                
                
                if i + 1 < n:
                    num_path[j][i] += num_path[j][i+1] 
                
                if j + 1 < m:
                    num_path[j][i] += num_path[j+1][i]
                    
        return num_path[0][0]
