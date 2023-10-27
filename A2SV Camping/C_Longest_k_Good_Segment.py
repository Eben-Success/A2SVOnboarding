from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))

l = 0
hashmap = defaultdict(int)
hashset = set()

for r in range(n):
    hashset.add(nums[r])
    hashmap[nums[r]] += 1
    
    while len():
        pass