n = int(input())

nums = list(map(int, input().split()))

res = 0
nums.sort()

i, j = 0, 0


for i in range(n):
    while j < n and nums[j] - nums[i] <= 5:
        j += 1
        res = max(res, j - i)

print(res)


    