import itertools

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        n = len(start)
        i = 0
        while i < n:
            if start[i] != end[i]:
                if i + 1 < n:
                    if start[i] + start[i+1] == 'XL':
                        if not end[i] + end[i+1] == 'LX':
                            return False
                        i += 1
                    elif start[i] + start[i+1] == 'RX':
                        if not end[i] + end[i+1] == 'XR':
                            return False
                        i += 1
                    else:
                        return False
                else:
                    return False
            i += 1
        return True
        '''
        
        for (i, x), (j, y) in  itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'), 
            ((j, y) for j, y in enumerate(end) if y != 'X'), 
            fillvalue=(None, None)):
            
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False
            
        
        return True
                    
