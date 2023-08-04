from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        # Time: O(n) + O(n) -> O(n) | Space: O(n): len(hashmap)

        if k > len(nums) or k <= 0:
            return 0
        
        max_sum = cur_sum = 0
        hashmap = defaultdict(int)

        for r in range(k):
            hashmap[nums[r]] += 1
            cur_sum += nums[r]

        if len(hashmap) == k:
            max_sum = cur_sum

        for r in range(k, len(nums)):
            hashmap[nums[r]] += 1
            rem = nums[r-k]
            hashmap[rem] -= 1

            if hashmap[rem] == 0:
                hashmap.pop(rem)

            cur_sum += nums[r]
            cur_sum -= rem

            if len(hashmap) == k:
                max_sum = max(max_sum, cur_sum)

        return max_sum


    """
    DS: hashmap

    Edge case: return 0 when k > len(nums) or <= 0

    Intuition
    1. Iterate over k:
      i. Store the elem in hashmap.
      ii. Increment cur_sum by nums[r]

    if len(hashmap) == k: means we have k unique elems
    so update max_sum

    2. Iterate from k to len(nums):
        i. Store right elem in hashmap.
        ii. remove the left elem from hashmap.
        iii. if left elem == 0: pop from hashmap.

        iv. increment cur_sum by nums[r]
        v. decrement by nums[l]
        vi. update max_sum
    
    """
            
