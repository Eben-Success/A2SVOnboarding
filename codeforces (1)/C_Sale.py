n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

res = 0


for num in nums:
    if num < 0:
        res += abs(num)
        m -= 1

        if m == 0:
            break

print(res)