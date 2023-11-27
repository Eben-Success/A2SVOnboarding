class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row, col = len(image), len(image[0])
        
        visited = set()

        original_image = image[sr][sc]

        def is_valid(r,c):
            row_inbound =  0 <= r < row
            col_inbound = 0 <= c < col

            if not row_inbound or not col_inbound:
                return False
            if (r, c) in visited or image[r][c] != original_image:
                return False

            return True

        directions = ((1,0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):

            if not is_valid(r, c):
                return

            visited.add((r, c))
            
            image[r][c] = color
            for dr, dc in directions:
                dfs(dr + r, dc + c)

        for r in range(row):
            for c in range(col):
                if (r, c) == (sr, sc):
                    dfs(r, c)

        return image
        
