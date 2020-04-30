class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        right_one = -1
        left_one = -1
        ans = 0
        
        for idx, val in enumerate(seats):
            right_one = -1
            if val:
                left_one = idx
            if not val:
                for idx1 in range(idx, n):
                    if seats[idx1]:
                        right_one = idx1
                        break
                if left_one >= 0 and right_one >= 0:
                    ans = max(ans, min(idx - left_one, right_one - idx))
                elif left_one >= 0:
                    
                    ans = max(ans, idx - left_one)
                elif right_one >= 0:
                    ans = max(ans, right_one - idx)
                
        return ans
