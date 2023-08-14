class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Optimal Approach
        # Time: O(n) | Space: O(n) : len(hashmap)

        #Edge case: Add 0 to the hashmap
        hashmap = {0: 1}
        count = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            diff = cur_sum - k
            count += hashmap.get(diff, 0)

            hashmap[cur_sum] = 1 + hashmap.get(cur_sum, 0)

        return count







        """
        1. We set two pointers i and j.
        2. Both pointers starts at the same index. (i==j)
        3. Move j until total == k, and we increment count by 1.
        4. Return count
        """
        # # Time: O(n^2) | Space: O(1)
        # # Brute Force
        # n = len(nums)
        # total = 0
        # count = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        # return count
