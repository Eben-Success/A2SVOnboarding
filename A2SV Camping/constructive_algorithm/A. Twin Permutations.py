t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    b = []
    
    for i in range(n):
        b.append(n - nums[i] + 1)
        
    print(*b)
