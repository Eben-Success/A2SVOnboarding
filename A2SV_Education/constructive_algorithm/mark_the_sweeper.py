t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    count = 0
    flag = False
        
    for i in range(n-1):
        if nums[i] > 0:
            flag = True
            count += nums[i]
            
        elif flag:
            if nums[i] == 0:
                count += 1
    
    print(count)
