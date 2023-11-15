from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = defaultdict(int)

        for word in words:
            hmap[word] += 1
        
        arr = [[-val, key] for key, val in hmap.items()]
        heapify(arr)

        res = []
        while k > 0:
            ans = heappop(arr)
            res.append(ans[1])
            k -= 1
        return res
