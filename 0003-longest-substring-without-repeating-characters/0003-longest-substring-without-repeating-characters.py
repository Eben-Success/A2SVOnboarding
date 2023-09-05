class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hashset = set()
        max_char = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            max_char = max(max_char, r - l + 1)
            
        return max_char
        