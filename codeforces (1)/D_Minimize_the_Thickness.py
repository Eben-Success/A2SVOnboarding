from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(int, input().split())

    res = l = 0
    hashmap = defaultdict(int)

    