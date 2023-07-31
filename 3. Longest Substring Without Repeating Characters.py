from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # Time: O(n) | Space: O(n)

        p_hash = defaultdict(int)

        for char in p:
            p_hash[char] += 1

        l = 0
        res = []
        temp = defaultdict(int)

        for r in range(len(s)):
            if s[r] in p_hash:
                temp[s[r]] += 1

            if temp == p_hash and len(temp) == len(p_hash):
                res.append(l)

            if r - l + 1 == len(p):
                if s[l] in temp:
                    temp[s[l]] -= 1

                    if temp[s[l]] == 0:
                        del temp[s[l]]

                l += 1

        return res


        #Intuition

                """
        1. Use hashmap to store p.
        2. temp hashmap to store anagrams of p.
        p = {a: 1, b: 1, c: 1}

        l = 0 
        move l by 1

        if s[l]
        r

        res = [0, ]

        if key in p_hash
        temp = {c: 1, b: 1, a: }
        reset temp = {}

        """
