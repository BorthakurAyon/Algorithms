class Solution:
    
    
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        self.skip = [[None for _ in range(10)]for _ in range(10)]
        
        
        self.skip[1][3], self.skip[3][1] = 2, 2
        self.skip[1][7], self.skip[7][1] = 4, 4
        self.skip[3][9], self.skip[9][3] = 6, 6
        self.skip[7][9], self.skip[9][7] = 8, 8
        self.skip[2][8], self.skip[8][2] = 5, 5
        self.skip[4][6], self.skip[6][4] = 5, 5
        self.skip[1][9], self.skip[9][1] = 5, 5
        self.skip[3][7], self.skip[7][3] = 5, 5
        
        result = 0
        
        for max_len in range(m, n + 1):
            visited = [False for _ in range(10)]
            result += self.dfs(1, visited, max_len) * 4 + self.dfs(2, visited, max_len) * 4 + self.dfs(5, visited, max_len)
                
        return result
    
    def dfs(self, cur, visited, remain):
        
        if remain == 1:
            return 1
        visited[cur] = True
        ret=0
        for node in range(1, 10):
            if not visited[node] and (self.skip[cur][node] is None or visited[self.skip[cur][node]]):
                ret += self.dfs(node, visited, remain - 1)
        visited[cur] = False
        
        return ret
