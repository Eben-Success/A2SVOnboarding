t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    l, r = 0, len(nums) - 1

    if len(nums) <= 2:
        print(*nums)
        continue

    while l <= r:
        print(nums[l], end=" ")
        l += 1

        if l <= r:
            print(nums[r], end=" ")
            r -= 1

    print()
