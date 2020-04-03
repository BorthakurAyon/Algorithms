class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        max_area = 0
        len_height = len(height)
        prev_h = 0
        tmp_h = 0
        tmp_area = 0
        for idx_start, value_start in enumerate(height):
            for idx_end, value_end in enumerate(height[idx_start + 1:][::-1]):
                tmp_h = min(value_start, value_end)
                if prev_h < tmp_h:
                    prev_h = tmp_h
                    tmp_area = prev_h * (len_height - idx_end - idx_start - 1)
                    if max_area < tmp_area:
                        max_area = tmp_area
        return max_area          
        '''
        
        max_area = 0
        area = 0
        x = 0
        y = len(height) - 1
        
        while (x < y):
            if height[x] <= height[y]:
                area = height[x] * (y - x)
                x += 1
            elif height[y] < height[x]:
                area = height[y] * (y - x)
                y -= 1
            
            max_area = max(max_area, area)
        
        return max_area
