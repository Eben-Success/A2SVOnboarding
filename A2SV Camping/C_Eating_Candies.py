t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = nums[0]
    suffix[-1] = nums[-1]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]
        
    idx = n  - 2

    while idx >= 0:
        suffix[idx] = suffix[idx+1] + nums[idx]
        idx -= 1

    l, r = 0, n - 1
    max_count = 0


    while l < len(nums) and r >= 0 and l < r:
        
        if prefix[l] == suffix[r]:
            max_count = max(max_count, (l + 1 + (n - r)))
            l += 1
            r -= 1
    
        elif prefix[l] < suffix[r]:
            l += 1 
        else:
            r -= 1
            
                
    print(max_count)

