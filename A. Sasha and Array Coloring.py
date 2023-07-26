t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    
    nums.sort()
 
    l, r = 0, len(nums) -1
    max_sum  = 0
    while l < r:
        max_sum += (nums[r] - nums[l])
        l += 1
        r -= 1
 
    
    print(max_sum)
