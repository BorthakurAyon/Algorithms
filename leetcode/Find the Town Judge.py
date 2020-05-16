from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        notjudge = defaultdict(lambda: [0, 0])
        for x, y in trust:
            notjudge[x][0] = 1
            notjudge[y][1] += 1
            
        for i in range(1, N+1):
            if not notjudge[i][0] and notjudge[i][1] == N -1:
                return i
        return -1 
