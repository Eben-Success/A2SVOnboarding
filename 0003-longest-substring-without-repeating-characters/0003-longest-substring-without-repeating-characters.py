class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            hashset.add(s[r])

        return longest
        