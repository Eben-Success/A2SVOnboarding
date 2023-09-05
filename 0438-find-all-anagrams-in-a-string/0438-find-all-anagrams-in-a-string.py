from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []
        start, end = len(p), len(s)

        if start > end:
            return res
        pmap = defaultdict(int)
        smap = defaultdict(int)
        l = 0
        

        for char in p:
            pmap[char] += 1
        
        for i in range(start):
            smap[s[i]] += 1

        if smap == pmap:
            res.append(l)

        for i in range(start, end):
            smap[s[i]] += 1
            smap[s[l]] -= 1

            if smap[s[l]] == 0:
                del smap[s[l]]


            if smap == pmap:
                res.append(l + 1)
            
            l += 1

        return res


        