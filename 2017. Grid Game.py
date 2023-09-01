class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0]) 
        res = float("inf")

        suffix = [0] * (n + 2)
        prefix = [0] * (n + 2)

        for i in range(len(suffix) - 2, 0, -1):
            suffix[i] = suffix[i+1] + grid[0][i-1]
        

        for i in range(1, len(prefix) - 1):
            prefix[i] = prefix[i-1] + grid[1][i-1]

        for i in range(1, len(suffix) - 1):
            res = min(res, max(prefix[i-1], suffix[i+1]))

        return res
