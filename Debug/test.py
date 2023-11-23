"""
create a matrix with 
1 2 2 1
2 4 2 4
2 2 3 1
2 4 2 4
"""



def findSum(board, row, col):
    max_sum = 0
    n = len(board)
    m = len(board[0])
    
    def is_valid(i, j):
        return i >= 0 and i < n and j >= 0 and j < m
            
    def reset_board(row, col):
        return row, col
    
    def add_sum(i, j):
        nonlocal max_sum
        max_sum += board[i][j]
        return max_sum
    
    for i in range(n):
        for j in range(m):
    
            while is_valid(i, j):
                add_sum(i, j)
                i += 1
                j += 1
                
            i, j = reset_board(row, col)
            while is_valid(i, j):
                add_sum(i, j)
                i -= 1
                j -= 1
            
            i, j = reset_board(row, col)
            while is_valid(i, j):
                add_sum(i, j)
                i += 1
                j -= 1
                
            i, j = reset_board(row, col)
            while is_valid(i, j):
                add_sum(i, j)
                i -= 1
                j += 1
                
            return max_sum
"""
0 1 1
1 0 1
1 1 0
"""
    
matrix = [[1, 2, 2, 1], [2, 4, 2, 4], [2, 2, 3, 1], [2, 4, 2, 4]]
# matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
n = len(matrix)
m = len(matrix[0])
max_sum = 0   
for i in range(n):
    for j in range(m):
        max_sum = max(max_sum, findSum(matrix, i, j) - (3*matrix[i][j]))
print(max_sum)
    
    
    
    