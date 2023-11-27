class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Time: O(n^2) | Space: O(n^2)
        row, col = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            row_inbound = 0 <= r < row
            col_inbound = 0 <= c < col

            if not row_inbound or not col_inbound:
                return 0

            if grid[r][c] == "0":
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))
            dfs(r + 1, c) #move right
            dfs(r - 1, c) #move left
            dfs(r, c - 1) #move up
            dfs(r, c + 1) #move down
            return 1

        islands = 0
        for r in range(row):
            for c in range(col):
                if dfs(r, c):
                    islands += 1

        return islands
