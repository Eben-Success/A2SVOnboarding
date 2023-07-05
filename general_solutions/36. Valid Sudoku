from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        1. Create a helper function to traverse the board.
        2. Use hashset to keep track of the rows and columns.
        3. If any repetition in row or col, return False.
        4. For the 3x3 board, set their keys to (r//3) and (c//3).
        5. If any repetition: return False.
        5. Return True if all conditions are met.
        """
        
        # Time: O(9*9) => O(1) | Space: O(9*9) => O(1)
        
        # Call the helper function of the Sudoko board
        return self.isValid(board)
        
        
    def isValid(self, board):
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        subgrid = collections.defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]
                if cell == ".":
                    continue
                else:
                    if cell in row_set[r] or cell in col_set[c] or cell in subgrid[(r//3, c//3)]:
                        return False
                    row_set[r].add(cell)
                    col_set[c].add(cell)
                    subgrid[(r//3, c//3)].add(cell)
        return True
