class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []
        
        self.genUtils(n, n, "", results)
        
    
        return results
    
    def genUtils(self, left, right, tmp, results):
        
        if left == 0 and right == 0:
            results.append(tmp)
            
        if left > 0:
            self.genUtils(left - 1, right, tmp + '(', results)
            
        if right > left:
            self.genUtils(left, right - 1, tmp + ')', results)
        
