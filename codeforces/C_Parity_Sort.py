t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    s_nums = sorted(nums)
    
        
    """
    7 10 1 3 2
    1 2 3 7 10
    
    11 3 15 3 2
    2 3 3 11 15
    """
    
    count = 0
    for i in range(len(nums)):
        if (nums[i] % 2 == 0 and s_nums[i] % 2 == 0) or (nums[i] % 2 == 1 and s_nums[i] % 2 == 1):
            count += 1
            
    if count == len(nums):
        print("YES")
    else:
        print("NO")
        
        