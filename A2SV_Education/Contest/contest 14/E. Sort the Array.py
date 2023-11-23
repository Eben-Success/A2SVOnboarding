n = int(input())

nums = list(map(int, input().split()))

sorted_nums = sorted(nums)

first_idx, last_idx = -1, -1

for i in range(n):
    if nums[i] != sorted_nums[i]:
        first_idx = i
        break
    
for i in range(n - 1, -1, -1):
    if nums[i] != sorted_nums[i]:
        last_idx = i
        break
    
if first_idx == -1 and last_idx == -1:
    print("yes")
    print("1 1")
    
else:
    nums[first_idx:last_idx+1] = reversed(nums[first_idx:last_idx+1])
    ans = "yes"
    
    for i in range(n):
        if nums[i] != sorted_nums[i]:
            ans = "no"
    print(ans)
    if ans == "yes":
        print(first_idx+1, last_idx+1)
    

 
