from collections import defaultdict

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # Time: O(n) | Space: O(n) : len(hashmap) & len(res)

        hashmap = {}
        count = 0
        res = []

        for i in range(len(A)):
            if A[i] not in hashmap:
                hashmap[A[i]] = 1
            else:
                hashmap[A[i]] += 1
                count += 1

            if B[i] not in hashmap:
                hashmap[B[i]] = 1
            else:
                hashmap[B[i]] += 1
                count += 1
            res.append(count)

        return res
