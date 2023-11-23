
n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)

for i in range(n):
    if nums[i] != sorted_nums[i]:
        break
    
for j in range(n-1, -1, -1):
    if nums[j] != sorted_nums[j]:
        break
    
if i == n-1 and j == 0:
    print("yes")
    print(1, 1)
    
elif nums[i:j+1] == sorted_nums[i:j+1][::-1]:
    print("yes")
    print(i+1, j+1)
    
else:
    print("no")

