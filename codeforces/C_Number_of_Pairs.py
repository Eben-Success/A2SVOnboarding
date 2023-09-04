def count_pairs(nums, target):
    nums.sort()
    res = 0
    l, r = 0, len(nums) - 1
    
    while l < r:
        if nums[l] + nums[r] <= target:
            res += r - l 
            l += 1
        else:
            r -= 1
            
    return res

def solve():
    n, l , r = map(int, input().split())
    nums = list(map(int, input().split()))
    upper = count_pairs(nums, l - 1)
    lower = count_pairs(nums, r)
    count = lower - upper
    return count
    
for _ in range(int(input())):
    print(solve())