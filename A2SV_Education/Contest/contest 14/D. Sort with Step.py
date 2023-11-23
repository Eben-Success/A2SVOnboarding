t = int(input())

for _ in range(t):
    len_nums, divisor = map(int, input().split())
    nums = list(map(int, input().split()))
    
    count = 0
    
    for i in range(len_nums):
        if (nums[i] - i - 1) % divisor != 0:
            count += 1
            
    if count == 0:
        print(0)
    elif count <= 2:
        print(1)
    else:
        print(-1)
            
            
