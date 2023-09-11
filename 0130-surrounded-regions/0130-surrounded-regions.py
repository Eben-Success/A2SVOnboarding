class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row, col = len(board), len(board[0])

        # create dfs to traverse the grid

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col and board[r][c] == "O"):
                return

            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # convert border Os to T
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r in [0, row - 1] or c in [0, col - 1]):
                    dfs(r, c)

        # convert remaining Os to X
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # convert Ts to Os
        for r in range(row):
            for c in range(col):
                if board[r][c] == "T":
                    board[r][c] = "O"
        