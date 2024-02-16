def solve(nums, k):
    
    res = ""
    
    for i in range(30, -1, -1):
        count = 0
        
        for num in nums:
            if num & (1 << i) == 0:
                count += 1
        if count <= k:
            res += "1"
            k -= count
        else:
            res += "0"
            
    return int(res, 2)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums, k))
