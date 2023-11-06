t = int(input())
 
for _ in range(t):
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    
    if sum(nums) < s:
        print(-1)
        continue
        
 
    l = 0
    max_len = 0
    total = 0
    
    for r in range(n):
        total += nums[r]
        
        #condition
        while total > s:
            total -= nums[l]
            l += 1
        max_len = max(max_len, r - l + 1)
    print(n - max_len)
