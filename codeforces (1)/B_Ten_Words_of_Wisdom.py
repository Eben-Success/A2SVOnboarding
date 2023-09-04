t = int(input())

for _ in range(t):
    nums = []  
    n = int(input())
    
    for _ in range(n):
        a, b = map(int, input().split())  
        nums.append((a, b))
    
    id = 0
    max_ = 0
    
    for idx, num in enumerate(nums):
        if num[0] <= 10:
            if num[1] >= max_:
                max_ = num[1]
                id = idx + 1
                
    print(id)
