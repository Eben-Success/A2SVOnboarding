t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    low, high = 0, min(a, b)
    
    n_teams = 0
    while low <= high:
        mid = (low + high)//2
        
        if 4 * mid > (a + b):
            high = mid - 1
        
        elif 4 * mid <= (a + b):
            n_teams = mid
            low = mid + 1
            
    print(n_teams)
