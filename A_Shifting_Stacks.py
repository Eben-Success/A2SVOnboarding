t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0, 0)
    flag = False
    for i in range(1, n):
        if nums[i] < i:
            flag = True
            break
        nums[i+1] += nums[i] - i
    
    if flag:
        print("NO")
    else:
        print("YES")