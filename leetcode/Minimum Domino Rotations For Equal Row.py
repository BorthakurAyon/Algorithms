class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        len_list = len(A)
        
        na = 0
        nb = 0
        
        na_top = 0
        na_bottom = 0
        
        nb_top = 0
        nb_bottom = 0
        
        
        a0, b0 = A[0], B[0]
        
        
        for a, b in zip(A, B):
        
            if ((a == a0) or (b == a0)) and na is not None:
                na += 1
            else:
                na = None
                
            if ((a == b0) or (b == b0)) and nb is not None:
                nb += 1
            else:
                nb = None
        
            if na is not None:
                
                if a != a0:
                    na_top += 1
                if b != a0:
                    na_bottom += 1
            
            if nb is not None:
                
                if a != b0:
                    nb_top += 1
                if b != b0:
                    nb_bottom += 1
        
        if na is None and nb is None:
            return -1
        elif na == len_list:
            return min(na_top, na_bottom)
        elif nb == len_list:
            return min(nb_top, nb_bottom)
        else:
            return -1
