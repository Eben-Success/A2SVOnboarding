#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        row, col = len(self.matrix), len(self.matrix[0])
        
        self.prefix_matrix = [[0 for _ in range(col)] for _ in range(row)]
        
        # Build a prefix sum matrix
        for r in range(row):
            for c in range(col):
                self.prefix_matrix[r][c] = self.matrix[r][c]
                
                if r > 0:
                    self.prefix_matrix[r][c] += self.prefix_matrix[r-1][c]
                    
                if c > 0:
                    self.prefix_matrix[r][c] += self.prefix_matrix[r][c-1]
                    
                if r > 0 and c > 0:
                    self.prefix_matrix[r][c] -= self.prefix_matrix[r-1][c-1]
                            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            
        if row1 == 0:
            row1 = 1
                        
        elif col1 == 0:
            col1 = 1
            
        sumRange = self.prefix_matrix[row2][col2] - self.prefix_matrix[row1- 1][col2] - self.prefix_matrix[row2][col1-1] + self.prefix_matrix[row1-1][col1-1]        

        return sumRange
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

