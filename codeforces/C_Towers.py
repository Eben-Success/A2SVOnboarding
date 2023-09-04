from collections import defaultdict
n = int(input())

res = []
hashmap = defaultdict(int)

nums = list(map(int, input().split()))

dist = len(set(nums))

for num in nums:
    hashmap[num] += 1
    
max_ = max(list(hashmap.values()))

print(max_, dist)

