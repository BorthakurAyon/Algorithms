class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        dist = 0
        for item in format(x^y, 'b'):
            
            if int(item):
                dist += 1
                
        return dist
