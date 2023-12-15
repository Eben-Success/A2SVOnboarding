class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row, col = len(mat), len(mat[0])
        res = [[0 for _ in range(col)] for _ in range(row)]
        sources = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        def is_valid(r, c):
            row_inbound = 0 <= r < row
            col_inbound = 0 <= c < col
            return row_inbound and col_inbound and mat[r][c] == 1

        while queue:
            r, c, dist = queue.popleft()

            if mat[r][c] == 0:
                res[r][c] = 0
            else:
                res[r][c] = dist

            for dr, dc in directions:
                if is_valid(dr + r, dc + c) and (dr + r, dc + c) not in visited:
                    queue.append((dr + r, dc + c, dist + 1))
                    visited.add((dr + r, dc + c))

        return res

            

            



        
