class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        visited = set()
        border_lands, lands = 0, 0

        def dfs(r, c):
            row_inbound = 0 <= r < row
            col_inbound = 0 <= c < col
            if not row_inbound or not col_inbound:
                return 0

            if (r, c) in visited:
                return 0
            if not grid[r][c]:
                return 0

            visited.add((r, c))
            count = 1
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for r in range(row):
            for c in range(col):
                lands += grid[r][c]

                if grid[r][c] not in visited and grid[r][c] and (r in [0, row - 1] or c in [0, col - 1]):
                    border_lands += dfs(r, c)

        return lands - border_lands
        