class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        n = len(coordinates)
        if n < 3:
            return True
        
        if (coordinates[1][0] - coordinates[0][0]):
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        else:
            slope = float("inf")
        for x, y in coordinates[2:]:
            
            
            if slope != (y - coordinates[0][1])/(x - coordinates[0][0]) and slope != float("inf"):
                return False       
            elif  slope == float("inf") and (x - coordinates[0][0]):
                return False
            
        return True
        
