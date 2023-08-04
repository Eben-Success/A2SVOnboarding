from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash_1 = defaultdict(int)
        hash_2 = defaultdict(int)

        for char in s1:
            hash_1[char] += 1

        l = 0

        for r in range(len(s2)):
            hash_2[s2[r]] += 1
            
            if r - l + 1 == len(s1):
                if hash_1 != hash_2:
                    hash_2[s2[l]] -= 1
                    if hash_2[s2[l]] == 0:
                        hash_2.pop(s2[l])
                    l += 1

                else:
                    return True
        return False
