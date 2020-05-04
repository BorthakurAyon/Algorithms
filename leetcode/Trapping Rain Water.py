class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        
        left = [0 for _ in range(n+1)]
        right = [0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            left[i] = max(left[i-1], height[i-1])
            
        for i in range(n-1, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(n):
            
            result += max(0, min(left[i], right[i+1]) - height[i])
            
        return result
