class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        
        adj = [[] for _ in range(N)]
        
        for x, y in dislikes:
            
            adj[x - 1].append(y - 1)
            adj[y - 1].append(x - 1)
            

        color = [0 for _ in range(N)]
            
        
        for i in range(N):
            
            
            if color[i] != 0: continue
                
            bfs = deque()
            bfs.append(i)
            
            color[i] = 1
            
            while bfs:
                
                item = bfs.popleft()
            
                for nei in adj[item]:
                    
                    if color[nei] != 0:
                
                        if color[item] == color[nei]: 
                            return False

                    else:
                        color[nei] = -color[item]
                        bfs.append(nei)

                
        return True
