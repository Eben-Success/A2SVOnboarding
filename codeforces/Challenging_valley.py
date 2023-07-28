from typing import List

def is_valley(n: int, nums: List[int]) -> str:
    up = False
    found = True

    for i in range(n - 1):
        if nums[i + 1] > nums[i]:
            up = True

        if nums[i + 1] < nums[i] and up:
            found = False

    ans = "YES" if found else "NO"
    return ans

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(is_valley(n, nums))
