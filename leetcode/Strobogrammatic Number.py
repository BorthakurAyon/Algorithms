class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        n = len(num)
        if not n: return False
        if n == 1 and num not in ['0', '1', '8']: return False
        
        strobo_list = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        
        i, j = 0, n-1
        
        while(i < j):
            if i != 0 and j != n-1 and (num[i], num[j]) == ('0', '0'): 
                i += 1
                j-= 1
                continue
            if (num[i], num[j]) not in strobo_list:
                return False
            
            i += 1
            j -= 1
        if n % 2 and num[i] not in ['0', '1', '8']: return False
        return True
