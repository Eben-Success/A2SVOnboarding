class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        """
        [1,2,3],
        [4,5,6]
        [7,8,9]

        [(0, 0), (0, 1), (0, 2)
         (1, 0), (1, 1), (1, 2)
         (2, 0), (2, 1), (2, 2)]

         (0, 0), (1, 0), (2, 0)
         (0, 1), (1, 1), (2, 1)
         (0, 2), (1, 2), (2, 2)

         matrix transpose affect the shape of the matrix.
         so we create a new matrix using [0 for _ in range(row)] for _ in range(col) instead of using [0 for _ in range(col)] for _ in range(row)
        """

        row, col = len(matrix), len(matrix[0])

        transpose_matrix = [[0 for _ in range(row)] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                transpose_matrix[j][i] = matrix[i][j]
        return transpose_matrix