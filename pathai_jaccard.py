'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy as np
mat = np.ones((3, 3)).tolist()
querry = [(0, 0, 1, 1), (1, 1, 2, 2)]

def compute_jaccard():
    union_val = 0
    intersect_val = 0
    pt_dict = {}
    for i in range(querry[0][0], querry[0][2] + 1):
        for j in range(querry[0][1], querry[0][3] + 1):
            pt_dict[(i, j)] = mat[i][j]
            union_val += mat[i][j]
        
    for i in range(querry[1][0], querry[1][2] + 1):
        for j in range(querry[1][1], querry[1][3] + 1):
            if (i, j) in pt_dict:
                intersect_val += mat[i][j]
            else:
                pt_dict[(i, j)] = mat[i][j]
                union_val += mat[i][j]
    print(pt_dict)
    
    return intersect_val/max(union_val, 1)
    
    
jaccard = compute_jaccard()
print(jaccard)
