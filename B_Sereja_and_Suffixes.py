n, m = map(int, input().split())

count = {} 
nums = list(map(int, input().split()))

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

total = len(set(nums))

for _ in range(m):
    l = int(input())
    if l == 1:
        print(total)
        continue
    num = nums[l-2]
    
    count[num] -= 1
    if count[num] == 0:
        del count[num]
        
    print(len(count))
    
    
    
    
    
    