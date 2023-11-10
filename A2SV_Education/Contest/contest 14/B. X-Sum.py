def findXSum(matrix, r, c):   
    total_sum = 0
    row, col = r, c
    
    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def reset_board(row, col):
        return row, col
    
    r, c = reset_board(row, col)
    while is_valid(r, c):
        total_sum += matrix[r][c]
        r += 1
        c += 1
        
    r, c = reset_board(row, col)  
    while is_valid(r, c):
        total_sum += matrix[r][c]
        r -= 1
        c += 1
    
    r, c = reset_board(row, col)
    while is_valid(r, c):
        total_sum += matrix[r][c]
        r -= 1
        c -= 1
        
    r, c = reset_board(row, col)
    while is_valid(r, c):
        total_sum += matrix[r][c]
        r += 1
        c -= 1
    r, c = reset_board(row, col)  
    return total_sum - (3 * matrix[r][c])
        
t = int(input())  
  
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        nums = list(map(int, input().split()))
        matrix.append(nums)
        
    max_sum = 0
    
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, findXSum(matrix, i, j))
    print(max_sum)
