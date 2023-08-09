from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:

        # Time: O(n) | Space: O(n) : len(odd), hashmap == O(26) == O(1)

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

        """
        In order to form the longest palindrome,
        1. We need to get the occurances of the chars in a hashmap.
        2. Group the chars by even and odd.
        3. res += all even
        4. res += each odd_num - 1
        5. Set flag to true
        6. If flag is true: res += 1 and return
        """

