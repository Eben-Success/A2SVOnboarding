from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        sorted_hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        idx = 0
        res = []
        while k > 0 and idx < len(sorted_hashmap):
            res.append(sorted_hashmap[idx][0])
            k -= 1
            idx += 1
        return res

        