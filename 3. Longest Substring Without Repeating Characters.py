class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # Time: O(n) | Space: O(n)
        
        l, r = 0, 0
        hashset = set()
        max_len = 0

        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])

                max_len = max(max_len, r - l + 1)
                r += 1

            else:
                hashset.remove(s[l])
                l += 1

        return max_len

        """
        Intuition

        Use a hashset.

        Iterate over s and store in set.
        IF not in set add cur num.
        find the max_len.
        ELSE:  remove l pointer from set.
        l += 1

        return max_len
        """




        
