t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    cur_sum = 0
    res = 0
    for i in range(k-1, -1, -1):
        if cur_sum + n - nums[i] < n:
            cur_sum += n - nums[i]
            res += 1
        
    print(res)
        
        
    
    