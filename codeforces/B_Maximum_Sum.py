t = int(input())

for _ in range(t):
    n, k = map(int, input().split())


    nums = list(map(int, input().split()))
    nums.sort()

    res = 0

    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):

        prefix[i+1] = prefix[i] + nums[i]

    for i in range(k + 1):
        res = max(res, prefix[len(nums) - (k - i)] - prefix[2*i])


    print(res)




