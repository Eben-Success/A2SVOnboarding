
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    for i in range(len(nums) -1):
        if abs(nums[i] - nums[i+1]) > 1:
            print("NO")
            break
    else:
        print("YES")