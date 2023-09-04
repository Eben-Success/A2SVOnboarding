t = int(input())

for _ in range(t):
    n = int(input())
    nums = input()
    
        
    l, r = 0, n - 1
    res = n
    
    while nums[l] != nums[r] and res > 0:
        l += 1
        r -= 1
        res -= 2
    print(res)
        
    
            
        