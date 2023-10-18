n = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
 
idx = 1
 
for num in nums:
    if num > idx:
        break
    else:
        idx += num
 
print(idx)
