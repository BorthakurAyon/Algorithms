class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.matrix = matrix
        # self.sum_map = {}
        

    def update(self, row: int, col: int, val: int) -> None:
        # tmp_val = self.matrix[row][col]
        self.matrix[row][col] = val
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row_idx in range(row1, row2+1):
            for col_idx in range(col1, col2+1):
                # self.sum_map[(row1, col1, row2, col2)] += self.matrix[row_idx][col_idx]
                sum += self.matrix[row_idx][col_idx]
                
        # return self.sum_map[(row1, col1, row2, col2)]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
