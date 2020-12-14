 '''
        
        while N:
            
            new_cells = [0] * 8
            
            for idx, val in enumerate(cells):
                cnt_0, cnt_1 = 0, 0
                
                if idx:
                    if cells[idx - 1]:
                        cnt_1 += 1
                    else:
                        cnt_0 += 1
                if idx < 7:
                    if cells[idx + 1]:
                        cnt_1 += 1
                    else:
                        cnt_0 += 1
                
                if cnt_0 == 2 or cnt_1 == 2:
                    new_cells[idx] = 1
                else:
                    new_cells[idx] = 0
                    
            cells = new_cells
            
            N -= 1
            
        return cells
        '''
        
        N = N % 14
        if not N:
            N = 14
            
        for _ in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells
