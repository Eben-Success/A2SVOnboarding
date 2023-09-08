class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        max_len = 0
        n = len(s)
        for i in range(n):
            # odd length

        # if n % 2 == 1:
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                window = (r - l + 1)
                if window > max_len:
                    max_len = window
                    res = s[l:r+1]
                l -= 1
                r += 1

        # else: # even length
            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                window = (r - l + 1)
                if window > max_len:
                    max_len = window
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res
        