from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Time: O(n) | Space: O(26) -> O(1)

        max_string = l = 0
        hashmap = defaultdict(int)
        
        for r in range(len(s)):
            hashmap[s[r]] += 1

            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1

                if hashmap[s[l]] == 0:
                    hashmap.pop(s[l])
                l += 1

            max_string = max(max_string, r - l + 1)
        
        return max_string
