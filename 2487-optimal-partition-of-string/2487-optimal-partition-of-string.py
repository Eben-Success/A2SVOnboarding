class Solution:
    def partitionString(self, s: str) -> int:

        l = 0
        hmap = {}
        count = 1

        for r in range(len(s)):
            if s[r] not in hmap:
                hmap[s[r]] = 1
            else:
                hmap = {}
                hmap[s[r]] = 1
                l = r
                count += 1

        return count
            
            
