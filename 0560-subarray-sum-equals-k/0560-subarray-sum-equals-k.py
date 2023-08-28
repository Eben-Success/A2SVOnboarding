class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashmap = {0: 1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num

            diff = prefix - k

            if diff in hashmap:
                count += hashmap[diff]

            hashmap[prefix] = 1 + hashmap.get(prefix, 0)

        return count
        