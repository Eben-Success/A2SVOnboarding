n = int(input())
nums = list(map(int, input().split()))

neg = 0
zero = 0
res = 0

for num in nums:
    if num < 0:
        res += abs(num + 1)
        neg += 1
        
    elif num > 0:
        res += abs(num - 1)
        
    else:
        res += 1
        zero += 1
        
if neg % 2 == 1 and not zero:
    res += 2
    
print(res)