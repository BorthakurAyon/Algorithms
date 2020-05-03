class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        results = []
        intervals = sorted(intervals)
        found = 0
        
        for start, end in intervals:
            
            found = 0
            
            if not len(results):
                results.append((start, end))
                
            else:
                for idx, (x, y) in enumerate(results):
                    if start >= y:
                        results[idx] = (x, end)
                        found = 1
                        break
                if not found:
                    results.append((start, end))
            
        
        
        return len(results)
