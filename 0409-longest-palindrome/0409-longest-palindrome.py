from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:

        """
        In order to form the longest palindrome,
        1. We need to get the occurances of the chars in a hashmap.
        2. Group the chars by even and odd.
        3. Pick all even and the max(odd)
        """

        hashmap = defaultdict(int)

        res = 0
        odd = []
        is_odd = False
        
        for char in s:
            hashmap[char] += 1

        for num in hashmap.values():
            if num % 2 == 0:
                res += num
            else: # num is odd
                res += num - 1
                is_odd = True

        if is_odd:
            res += 1

        return res

