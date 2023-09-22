n, t = map(int, input().split())

# num of books
# t = free times.

nums = list(map(int, input().split()))

nums.sort()
cur = nums[0]
count = 1
if cur > t:
    print(0)

for i in range(1, n):
    if cur + nums[i] >= t:
        break
    else:
        cur += nums[i]
        count += 1
        
print(count)
    