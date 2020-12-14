
def findmax(values, max_val):        
    res = -1

    for item in values:
        if item <= max_val and item > res:
            res = item

    if res > -1:
        values.remove(res)
        return res

    return None


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:           
        
        for max_x in [2, 1, 0]:
            

            values = A[:]
            
            
            x = findmax(values, max_x)
            
            
            if x is None:
                return ""
                
            
            if x == 2:
                max_y = 3
            else:
                max_y = 9
                
                
            y = findmax(values, max_y)
            

            if y is None:
                continue
                
            
            max_a = 5  
            a = findmax(values, max_a)
            
            if a is None:
                continue

            return "{}{}:{}{}".format(x,y,a,values[0])
                
                
        return ""
