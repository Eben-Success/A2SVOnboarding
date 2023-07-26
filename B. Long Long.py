t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    max_sum = 0
    flag = False
    count = 0
 
    for num in nums:
        max_sum += abs(num)
 
        if num < 0 and not flag:
              flag = True
              count += 1
 
        if num > 0:
             flag = False
 
    print(max_sum, count)
 
