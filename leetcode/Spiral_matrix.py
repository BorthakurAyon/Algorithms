class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        ans = []
        
        if not len(matrix): return ans
        
        
        m, n = len(matrix), len(matrix[0])
        
        i, left, j = 0, 0, n
        
        visited = [0] * m
        visited_col = [0] * n
        
        while sum(visited) <= m:
            
            if not visited[i]:
                ans.extend(matrix[i][left:j])
                visited[i] = 1    
            i += 1
            
            if j > 0 and not visited_col[j-1]:
                for _idx in range(i, m-1):
                    
                    ans.append(matrix[_idx][j-1])
                visited_col[j-1] = 1
            
            if not visited[m-1]:
                ans.extend(matrix[m-1][left:j][::-1])
                visited[m-1] = 1
                
            m -= 1
            
            if left < n and not visited_col[left]:
                for _idx in range(m-1, i + 1):                
                    ans.append(matrix[_idx][left])
                visited_col[left] = 1
            
            j -= 1
            left += 1
            
        return ans
        '''
        
        ans = []
        
        if not len(matrix):
            return ans
        
        m = len(matrix)
        n = len(matrix[0])
        
        if not n:
            return ans * m
        
        while len(matrix):
            
            ans.extend(matrix.pop(0))
            
            if not len(matrix):
                return ans
            
            for _item in matrix:
                ans.append(_item.pop(-1))
            
            matrix = list(filter(None, matrix)) 
                
            if not len(matrix):
                return ans
                
            ans.extend(matrix.pop(-1)[::-1])
            
            if not len(matrix):
                return ans
            
            for _item in matrix[::-1]:
                ans.append(_item.pop(0))
            matrix = list(filter(None, matrix)) 
            
        return ans
            
