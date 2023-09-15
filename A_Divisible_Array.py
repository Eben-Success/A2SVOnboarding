t = int(input())

for _ in range(t):
    n = int(input())
    
    res = []
    for i in range(1, n + 1):
        res.append(i*2)
        
    print(*res)
        