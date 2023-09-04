n = int(input())
nums = list(map(int, input().split()))
c = int(input())
n_bars = list(map(int, input().split()))

nums.sort(reverse=True)

total = sum(nums)

for num in n_bars:
    print(total - nums[num - 1])


