class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])


        def is_valid(r, c):
            row_inbound = 0 <= r < row
            col_inbound = 0 <= c < col
            if not row_inbound or not col_inbound:
                return False
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if not is_valid(r, c):
                return 0

            if (r, c) in visited:
                return 0

            if grid[r][c] == 0:
                return 0

            visited.add((r, c))

            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area

        max_area = 0
        for r in range(row):
            for c in range(col):
                max_area = max(max_area, dfs(r, c))

        return max_area

                
        
