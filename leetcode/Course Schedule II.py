from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        self.course_order = []
        
        self.visited = [False for _ in range(numCourses)]
        
        self.graph = defaultdict(list)
        
        for _x, _y in prerequisites:
            self.graph[_x].append(_y)
            
        for key, val in self.graph.items():
            
            for _val in val:
                
                if not self.graph[_val]:
                    
                    self.dfs(_val)
                    break
        
        if len(self.course_order) == numCourses:
            return self.course_order
        else:
            return []
        
        def dfs(self, val):


            if self.visited[val]: return 

            if not self.graph[val]:
                self.course_order.append(val)
                self.visited[val] = True

            else:
                for _val in self.graph[val]:
                    self.dfs(_val)
                    self.course_order.append(_val)
                    self.visited[_val] = True

            print(self.graph, val, self.course_order)

            return
        '''
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path
    
    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True
