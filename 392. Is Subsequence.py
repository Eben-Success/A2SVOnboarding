from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Solution 1
        # Time: O(n) | Space: O(n)
        t_hash = defaultdict(int)

        for char in t:
            t_hash[char] += 1

        for char in s:
            if char not in t_hash:
                return False

        return True


        Solution 2
        Time: O(n) | Space: O(1)

        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1

        return l == len(s)
