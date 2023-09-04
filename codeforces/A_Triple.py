from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
          
    
    nums.sort()
    count = 1
    n = len(nums)
    
    for i in range(n - 1):
        if nums[i] == nums[i+1]:
            count += 1
            
            if count >= 3:
                print(nums[i])
                break
            
        elif nums[i] != nums[i+1]:
            count = 1
            continue
        
    if count < 3:
        print(-1)